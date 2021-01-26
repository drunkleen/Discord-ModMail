import discord
from discord.ext import commands

##replace "DiscordBot_Token" with your bot token
TOKEN = "DiscordBot_Token" 

## use "!send" to call the bot in texxt-channel
client = commands.Bot(command_prefix=commands.when_mentioned_or("!send "), case_insensitive=True)
client.remove_command('help') # Help CMD 

def check_team(ctx):

    ## replace your Server ID and Role ID with "Server ID" and "Role ID"
    return client.get_guild(Server ID).get_role(Role ID) in ctx.author.roles 

@client.event
async def on_connect():
    print('DiscordMail DrunkLeen_v1.2')

@client.event
async def on_message(message):
    if message.author.id == client.user.id:
        return
    
    if message.author != message.author.bot:
        if not message.guild:
        
            ## replace your Server ID and Role ID with "Server ID" and "Channel ID"
            await client.get_guild(Server ID).get_channel(Channel ID).send(f"User meniton {message.author.mention}\nUsername: {message.author}\nUser-ID: {message.author.id}\n\n__**User Message:**__\n{message.content}")
    
    await client.process_commands(message)

@client.command()
@commands.check(check_team)
async def pm(ctx, member: discord.Member, *, text):
    await member.send(text)

@client.event # Bot reconnect
async def on_resumed():
    print('reconnected')
    
##replace "DiscordBot_Token" with your bot token
client.run(('DiscordBot_Token'), reconnect=True) # Bot reconnect


