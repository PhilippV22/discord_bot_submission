
import discord
from discord.ext import commands

client = commands.Bot(command_prefix="!", intents=discord.Intents.all())
Token = 'BOT_TOKEN'

@client.event
async def on_ready():
    print("Bot ist online!")
    print(f"We have logged in as {client.user}")
    await client.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name =f"{client.command_prefix}help"))
    print(discord.__version__)

async def status_task():
        await client.change_presence(activity=discord.Game("Test Bot von PhilippV"))

client.run(Token)
