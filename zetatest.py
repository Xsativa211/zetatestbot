import discord
from discord.ext.commands import Bot
from discord.ext import commands
import asyncio
import time
import random
import requests
import os
from discord import Game


Client = discord.client
client = commands.Bot(command_prefix = '!')
Clientdiscord = discord.Client()

    
@client.event
async def on_ready():
    await client.change_presence(game=Game(name='Project ZetaRO',))
    print('Codes are working perfectly fine! you may use it now!') 

@client.event
async def on_message(message):  
    if message.content == '!update':
        await client.send_message(message.channel,'We have new server update! \n \n \n \n \n \n \nhttps://tenor.com/view/happy-im-so-happy-happiness-joy-excited-gif-7525568')
    if ('!update') in message.content:
       await client.delete_message(message)       
        
client.run(str(os.environ.get('TOKEN')))
