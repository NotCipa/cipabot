import discord
from discord.ext.commands import Bot
from discord.ext import commands

Client = discord.Client()
bot_prefix= "|"
client = commands.Bot(command_prefix=bot_prefix)

@client.event
async def on_ready():
    print("Bot Online!")
    print("Name: {}".format(client.user.name))
    print("ID: {}".format(client.user.id))


#test command
@client.command(pass_context = True)
async def info(ctx):
    await client.say("Cipa is better than NotCipa!")

@client.event
async def on_message(message):
    if message.content.startswith ("|ping"):
        await client.send_message(message.channel, "Pong!")
           if message.content.startswith ("|woomy"):
        await client.send_message(message.channel, "ngyes!")

client.run("NDU5NjIxMDc0OTA5NTI4MDk0.Dg44Dg.-KZ1-9RRdQGRz8hCtrupODSnJnI")

