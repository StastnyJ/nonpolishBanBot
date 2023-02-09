#!/usr/bin/python3

from langdetect import detect
import os
import discord
from dotenv import load_dotenv
import time

banTime = 300

load_dotenv()
TOKEN = os.getenv("DISCORD_TOKEN")

intents = discord.Intents.all()
client = discord.Client(intents=intents)

@client.event
async def on_message(message: discord.Message) -> None:
    if message.author == client.user:
        return
    if 'Czech' in [r.name for r in message.author.roles]:
        return
    if detect(message.content) != "pl":
        await message.delete()
        await message.channel.send("Mów po polsku, kurwa!")

@client.event
async def on_message_edit(before: discord.Message, after: discord.Message):
    if after.author == client.user:
        return
    if 'Czech' in [r.name for r in after.author.roles]:
        return
    if detect(after.content) != "pl":
        await after.delete()
        await after.channel.send("Mów po polsku, kurwa!")

client.run(TOKEN)