import discord
import asyncio
import random
import os

TOKEN = os.environ['TOKEN']
ROLE_NAME = "UR ROLE NAME HERE"    

intents = discord.Intents.default()
intents.guilds = True
intents.members = True

client = discord.Client(intents=intents)

@client.event
async def on_ready():
    print(f'Logged in as {client.user}')
    guild = client.guilds[0]
    
    role = discord.utils.get(guild.roles, name=ROLE_NAME)

    if not role:
        print("Rainbow role not found!")
        return

    while True:
        color = discord.Color(random.randint(0, 0xFFFFFF))
        await role.edit(color=color)
        await asyncio.sleep(10)

client.run(TOKEN)
