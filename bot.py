import discord
from discord.ext import commands


intents = discord.Intents.default()
intents.members - True

bot = commands.Bot(command_prefix="/",intents = intents)

@bot.event
async def on_ready():
    print(">> Bot is online<<")
    
@bot.event
async def on_member_join(member):
    channel = bot.get_channel(927211664170950656)
    await channel.send(F'{member} join!!')
    
@bot.command()
async def time(ctx):
    await ctx.send(F'{round(bot.latency*1000)}[毫秒]')
   
@bot.event
async def on_member_remove(member):
    print(F'{member} leave!!')
    
bot.run("OTI3MTg2MDk1NDc5ODY5NDYw.YdGjVw.bZKa8RCcG0LdVPs-dW3ZbnwMazc")
