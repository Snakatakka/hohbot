# This example requires the 'message_content' intent.

import discord # type: ignore
from functions import * 

# Discord.py variables
intents = discord.Intents.default()
intents.message_content = True
client = discord.Client(intents=intents)
user = client.user
hostRole = 1484317628230271189

# Non Discord.py varibles
initialized = False

listOfHosts = []
listOfCommands = ['sayHi', 'sayName', 'addRank']
listOfFunctions = ['Bot says hi!', "Bot says the message author's name", 'funky math']

ContestantRankDictionary = {
    
}



@client.event
async def on_ready():
    print(f'We have logged in as {client.user}')

@client.event
async def on_message(message):
    if message.author == user:
        return

    if message.content.startswith('hoh!'):
        if message.content.find('init') == 4:
            await message.channel.send('Beginning initialization sequence!')

        elif initialized == True:
            if message.content.find("sayHi") == 4:
                await message.channel.send(f'Hello!')
            
            elif message.content.find("sayName") == 4:
                await message.channel.send(f'Your username is {message.author}!')
            
            elif message.content.find("help") == 4:
                length = len(listOfCommands)
                fullHelpString = ""
                for i in range(0, length):
                    fullHelpString += f'{listOfCommands[i]} - {listOfFunctions[i]} \n'
                    await message.channel.send(f'{fullHelpString}')
            
            elif message.content.find("addRank") == 4:
                if hostRole in [hostRole for role in message.author.roles]:
                    rank(1, 2)
                else:
                    await message.channel.send('ERROR: Invalid permissions.')
                    
            else:
                await message.channel.send('ERROR: Invalid command, use the command "hoh!help" to view a list of all commands!')
        
        else:
            await message.channel.send(f'ERROR: Roles not initialized, Use the command "hoh!init" to begin the initialization process!')


client.run('TOKENID')
