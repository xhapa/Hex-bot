import os

import discord
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
GUILD = os.getenv('DISCORD_GUILD')

intents = discord.Intents().all()

client = discord.Client(intents=intents)

command_sym = '|'

@client.event
async def on_ready():
    for guild in client.guilds:
        if guild.name == GUILD:
            break
    print(
        f'{client.user} is connected to the following guild:\n'
        f'{guild.name}(id: {guild.id})'
    )

@client.event
async def on_member_join(member):
    await member.create_dm()
    await member.dm_channel.send(
        f'Hi {member.name}, welcome to Discord server!'
    )

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if 'happy birthday' in message.content.lower():
        await message.channel.send('Happy Birthday! 🎈🎉')
    
    elif message.content.startswith(command_sym):

        command = message.content.split()[0].replace(command_sym,"")

        if command == 'help':
            answer = discord.Embed(title="Tronte commands",
                                description=f"""Commands\n\n`Help` : **{'|help'}**\n`Hello` : **{'|hello'}**""",
                                colour=0x1a7794) 

            await message.channel.send(embed=answer)
        
        if command == 'hello':
            await message.channel.send(f'Hello {message.author.name}')


client.run(TOKEN)