from unicodedata import name
import discord
import random
from discord.ext import commands

intents = discord.Intents.default()

bot = commands.Bot(command_prefix='mi!', intents=intents)

with open('mica.txt', 'r') as f:
    micaurl = [line.strip() for line in f]

with open('acrylic.txt', 'r') as f:
    acrylicurl = [line.strip() for line in f]

with open('aero.txt', 'r') as f:
    aerourl = [line.strip() for line in f]

with open('real.txt', 'r') as f:
    realurl = [line.strip() for line in f]

@bot.event
async def on_ready():
    print(f'Logged in as {bot.user} (ID: {bot.user.id})')
    print('------')

@bot.command()
async def mica(ctx, *args):
    randomthing = random.choice(micaurl)
    urlorig = ctx.message.jump_url
    """cures blindness."""
    tingz = ' ' .join(args)
    embed=discord.Embed(title="mica dose for you :D")
    # Add author, thumbnail, fields, and footer to the embed
    embed.set_author(name="jump to original msg", url=urlorig)
    embed.set_image(url=randomthing)
    await ctx.send(embed=embed)
    embed2=discord.Embed(title="Were the results satisfying?", description="react with :thumbsup: or :thumbsdown:")
    await ctx.send(embed=embed2)

@bot.command()
async def acrylic(ctx, *args):
    randomthing = random.choice(acrylicurl)
    urlorig = ctx.message.jump_url
    """cures blindness."""
    tingz = ' ' .join(args)
    embed=discord.Embed(title="acrylic dose for you :(")
    # Add author, thumbnail, fields, and footer to the embed
    embed.set_author(name="jump to original msg", url=urlorig)
    embed.set_image(url=randomthing)
    await ctx.send(embed=embed)
    embed2=discord.Embed(title="Were the results satisfying?", description="react with :thumbsup: or :thumbsdown:")
    await ctx.send(embed=embed2)

@bot.command()
async def aero(ctx, *args):
    randomthing = random.choice(aerourl)
    urlorig = ctx.message.jump_url
    """cures blindness."""
    tingz = ' ' .join(args)
    embed=discord.Embed(title="aero dose for you :)")
    # Add author, thumbnail, fields, and footer to the embed
    embed.set_author(name="jump to original msg", url=urlorig)
    embed.set_image(url=randomthing)
    await ctx.send(embed=embed)
    embed2=discord.Embed(title="Were the results satisfying?", description="react with :thumbsup: or :thumbsdown:")
    await ctx.send(embed=embed2)

@bot.command()
async def realmica(ctx, *args):
    randomthing = random.choice(realurl)
    urlorig = ctx.message.jump_url
    """cures blindness."""
    tingz = ' ' .join(args)
    embed=discord.Embed(title="aero dose for you :)")
    # Add author, thumbnail, fields, and footer to the embed
    embed.set_author(name="jump to original msg", url=urlorig)
    embed.set_image(url=randomthing)
    await ctx.send(embed=embed)
    embed2=discord.Embed(title="Were the results satisfying?", description="react with :thumbsup: or :thumbsdown:")
    await ctx.send(embed=embed2)

@bot.event
async def on_reaction_add(reaction, user):
    if reaction.message.author.id == 936273651358117978:     #checks if message is from bot
        if reaction.emoji == '👍':
            #process for this reaction
            print("u reacted with :thumbsup:")
            for user in await reaction.users().flatten():
                await reaction.remove(user)
        if reaction.emoji == '👎':
            print("u reacted with :thumbsdown:")
            ctx = bot.get_channel(reaction.message.channel.id)
            await ctx.send("I notified <@829434032508108820> about that, he'll change that soon. Here's your message link if needed. " + reaction.message.jump_url)
            for user in await reaction.users().flatten():
                await reaction.remove(user)
    else:
        return

@bot.command()
async def suggest(ctx, *args):
    embed2=discord.Embed(title="Where do I send my mica suggestions?", description="send your suggestions [in this form.](https://forms.gle/DpwNBZtBozxov8Hp7), keep in mind that they will be manually reviewed before they're added.")
    await ctx.send(embed=embed2)

@bot.command()
async def feedback(ctx, *args):
    embed2=discord.Embed(title="Where do I send my feedback?", description="send your feedback [in Developer Sanctuary.](https://discord.gg/msA2TwFvR5)")
    await ctx.send(embed=embed2)

bot.run('YOURTOKEN')
