import discord
from discord.ext import commands
import os
from dotenv import load_dotenv

load_dotenv()

TOKEN = os.getenv('DISCORD_TOKEN')

intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix='!', intents=intents)

@bot.event
async def on_ready():
    print(f'Bot conectado com sucesso como: {bot.user}')

@bot.command(name='hello') #!hello
async def hello(ctx):
    await ctx.send('Olá! Sou um bot de teste. Como posso ajudar?')

bot.run(TOKEN)