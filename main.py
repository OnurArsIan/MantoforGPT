import os

import discord

import openai

from keep_alive import keep_alive

TOKEN = os.environ['DISCORD_TOKEN']
openai.api_key= os.environ['OPENAI_KEY']


intents=discord.Intents.all()
client=discord.Client(command_prefix='!',intents=intents)

@client.event

async def on_ready():
    print("Signed in with {0.user} account ".format(client))

@client.event



async def on_message(message):
    if message.author== client.user:
        return
    if client.user in message.mentions:
        response=openai.Completion.create(
        engine='text-davinci-003',
        prompt=f"{message.content}",
        temperature=0.7,
        max_tokens=2048,
        
    )
    await message.channel.send(response.choices[0].text)


keep_alive()
client.run(TOKEN)
