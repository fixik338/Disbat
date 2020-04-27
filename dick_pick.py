import discord
from discord.ext import commands

TOKEN = 'NzA0MDc4MDQyMDk5ODc1OTQx.XqX-gg.Ia7aloZqH_-PEuj2NjBLaJkbTQ8'
bot = commands.Bot(command_prefix='!')  # инициализируем бота с префиксом '!'


@bot.command(pass_context=True)
async def test(ctx, arg):
    await ctx.send(arg)


@bot.command(pass_context=True)
async def pisya(ctx, arg):
    await ctx.send(arg)


bot.run(TOKEN)
