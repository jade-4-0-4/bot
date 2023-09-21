import discord
from discord.ext import commands
import chill

cogs = [chill]

client = commands.Bot(command_prefix='?',intents = discord.Intents.all())

for i in range(len(cogs)):
    cogs [i].setup(client)


client.run("MTE0ODk0NjkzMTQ2MTEyODMwMw.GgGNNf.EhVytSqvcSnET81gFFCPsbHmwrTP6XtOMAgwBA")