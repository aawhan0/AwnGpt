import discord
from discord.ext import commands
import config

intents = discord.Intents.all()
bot = commands.Bot(command_prefix='!', intents=intents)

@bot.event
async def on_ready():
    print("--------the bot is now ready to use--------")
    await bot.tree.sync()

@bot.event
async def on_message(msg: discord.Message):
    content = msg.content

    print(content)

    if content == "hello":
        await msg.reply("hi hizru, kaisa hai?")

    if content == "manmohan":
        await msg.reply("ha bhai kitne plate poge lagadu?")

    await bot.process_commands(msg)
    
@bot.tree.command()
async def intro(interaction: discord.Interaction):
    await interaction.response.send_message("Hello, I am Aawhan's Bot.")

@bot.tree.command()
async def hizru(interaction: discord.Interaction):
    await interaction.response.send_message("Hello Hizruboy")

@bot.tree.command()
async def poha(interaction: discord.Interaction):
    await interaction.response.send_message("Did you mean Manmohan by any chance?")

bot.run(config.DISCORD_TOKEN)
