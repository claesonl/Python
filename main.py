import discord
import asyncio
import random
client = discord.Client()
bid = "215523928301371392"

@client.event
async def on_ready():
    print('De bot is successvol geladen als')
    print(client.user.name)
    print(client.user.id)
    print('--------------')



@client.event

async def on_message(message):
    if message.content.startswith('!server'):
        await client.send_message(message.channel, "```Over ons: \n Hey```")
    if message.content.startswith('!test'):
        await client.send_message(message.channel, "Dit is ook een test!")

    if message.content.startswith('?status'):
        game = message.content[8:]
        await client.change_presence(game=discord.Game(name=game, type=1))
        await client.send_message(message.channel, "De status zijn aangepast naar: " + game + "")

client.run('NDYwNzMyMjExNDc0MzMzNzE3.Dl9Cag.kv9nHOTP1990ujcTbqPDy6259yE')