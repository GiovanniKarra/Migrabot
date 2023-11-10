import os

from dotenv import load_dotenv
import discord
from discord.ext import commands


load_dotenv()

TOKEN = os.getenv("MIGRABOT_TOKEN")
INTENTS = discord.Intents.default()
INTENTS.message_content = True

bot = commands.Bot(command_prefix="/", intents=INTENTS)

MIGRABOT_CHANNEL = bot.get_channel(1172484129141575690)

@bot.event
async def on_ready():
    print(f"{bot.user} has connected to Discord!")

@bot.command()
async def todo(ctx, *arg):
    await ctx.message.delete()
    message = await ctx.send(f"TODO : {' '.join(arg)}")
    await message.add_reaction("✅")

@bot.event
async def on_reaction_add(reaction, user):
    if user.bot:
        return

    if reaction.message.content[:4] == "TODO" and reaction.emoji == "✅":
        await reaction.message.delete()

bot.run(TOKEN)