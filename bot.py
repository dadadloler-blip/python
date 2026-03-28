import discord
from discord.ext import commands
from model import get_class

# Diamo i permessi al bot
intents = discord.Intents.default()
intents.message_content = True
# creaimo il bot
bot = commands.Bot(command_prefix='$', intents=intents)
# qui inseriamo i comandi....
@bot.event
async def on_ready():
    print(f'Bot {bot.user} online')


@bot.command()
async def test(ctx):
    await ctx.send('Test OK')

@bot.command()
async def check(ctx):
    immagini = ctx.message.attachments
    if immagini:
        for immagine in immagini:
            file_name = immagine.filename
            print(file_name)
            file_url = immagine.url
            print(file_url)
            await immagine.save(f"img/{file_name}")
            percentuale, classe = get_class('keras_model.h5', 'labels.txt',f"img/{file_name}")
            if classe == 'Funghi':
                await ctx.send("e' commestibile")
            await ctx.send(f"L'immagine e' {classe}")
            await ctx.send(f"La percentuale di accuratezza e' {percentuale}")
    else:
        await ctx.send('Non ci sono immagini da salvare')

bot.run('')