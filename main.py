import discord
from discord.ext import commands
import requests
intents = discord.Intents().all()
bot = commands.Bot(command_prefix='!',intents=intents)

@bot.event
async def on_ready():
    print(f'Logged in as {bot.user.name} ({bot.user.id})')

@bot.command()
async def speedrun(ctx, game):
    api_url = f'https://www.speedrun.com/api/v1/games/{game}/records?top=1'
    response = requests.get(api_url)

    if response.status_code == 200:
        data = response.json()
        if data['data']:
            run = data['data'][0]['runs'][0]['run']
            player = run['players'][0]['id']
            time = run['times']['primary']
            await ctx.send(f'Current world record for {game}: {time} by {player}')
        else:
            await ctx.send('No records found for the specified game.')
    else:
        await ctx.send('Failed to fetch data from speedrun.com')

# Replace 'YOUR_BOT_TOKEN' with your actual bot token
bot.run('YOUR_BOT_TOKEN')
