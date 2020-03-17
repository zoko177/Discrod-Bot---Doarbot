import discord
import random
from apex_legends import ApexLegends

class apex_player():
    def __init__(self, name):
        self.name = name
        self.kills = 0

    def __repr__(self):
        return repr((self.name, self.kills))


client = discord.Client()

apex = ApexLegends("4d9fbf0f-f2db-47dd-8082-7d631d0b466e")
token = 'Njg3Njg2ODY0NDc1Mzg5OTUy.XmpZeQ.SwXWBr4Zz1MWjiCSC0cAJWmWr8w'
play_list_doar = []
err_msg = 'WRONG INPUT, DOAR BOT MAD'

@client.event
async def on_message(message):
    list_str = list(message.system_content.split(" "))
    if "!rand" in list_str:
        li = list_str.copy()
        li.remove('!rand')
        rand_user = []
        for i in range(len(li)):
            chosed = random.choice(li)
            rand_user.append(chosed)
            li.remove(chosed)
        await message.channel.send(str(rand_user))
    elif '!rand_active' in list_str:
        if len(list_str) != 1 :
            await message.channel.send(err_msg)
        else:
            if len(play_list_doar) == 0:
                await message.channel.send('Player list is empty')
            else:
                rand_gp = []
                for player in play_list_doar:
                    rand_gp.append(player.name)
                rand_gp_ch = []
                for i in range(len(rand_gp)):
                    chosed = random.choice(rand_gp)
                    rand_gp_ch.append(chosed)
                    rand_gp.remove(chosed)
                await message.channel.send(rand_gp_ch)
    elif '!flip' in list_str:
        coin = ['KA', 'KALO']
        await message.channel.send(random.choice(coin))

    elif '!create' in list_str:
        list_str.remove('!create')
        play_list_doar.append(apex_player(list_str[0]))
    elif '!ka' in list_str:
        list_str.remove('!ka')
        if len(list_str) != 2 or list_str[0].__class__ != ''.__class__ or  list_str[1].isdigit() == False :
            await message.channel.send(err_msg)
        else:
            found = 0
            for player in play_list_doar:
                if player.name == list_str[0]:
                    found = 1
                    player.kills += int(list_str[1])
            if found == 0 :
                await message.channel.send('Player not found')

    elif '!reset' in list_str:
        if len(list_str) != 2 or list_str[1].__class__ != '':
            await message.channel.send(err_msg)
        else:
            for player in play_list_doar:
                if player.name == list_str[1]:
                    player.kills = 0
    elif '!del' in list_str:
        if len(list_str) != 2 or list_str[1].__class__ != ''.__class__:
            await message.channel.send(err_msg)
        else:
            for player in play_list_doar:
                if player.name == list_str[1]:
                    play_list_doar.remove(player)

    elif '!reset_all' in list_str:
        if len(list_str) != 1:
            await message.channel.send(err_msg)
        else:
            for player in play_list_doar:
                player.kills = 0

    elif '!reset_db' in list_str:
        if len(list_str) != 1:
            await message.channel.send(err_msg)
        else:
            play_list_doar.clear()

    elif '!scb' in list_str:
        if play_list_doar == []:
            await message.channel.send('Player list is empty')
        elif len(list_str) != 1:
            await message.channel.send(err_msg)
        else:
            sorted_players = sorted(play_list_doar, key=lambda apex_player: apex_player.kills, reverse=True)
            await message.channel.send(sorted_players)

    elif '!score' in list_str:
        if play_list_doar == []:
            await message.channel.send('Player list is empty')
        elif len(list_str) != 2 or list_str[1].__class__ != ''.__class__:

            await message.channel.send(err_msg)
        else:
            found = 0
            for player in play_list_doar:
                if player.name == list_str[1]:
                    await message.channel.send('Player name: '+player.name+' Kills: '+str(player.kills))
                    found = 1
            if found == 0:
                await message.channel.send('Player not exits')

    elif '!stats' in list_str:
        if len(list_str) != 2 or list_str[1].__class__ != ''.__class__:
            await message.channel.send(err_msg)
        else:
            apex_profile = apex.player(list_str[1])
            await message.channel.send ('Apex Nick: ' + apex_profile.username +' LvL: ' +apex_profile.level + ' Total Kills: ' + apex_profile.kills + ' Total Damage: ' + apex_profile.damage)

    elif '!omri' in list_str:
        apex_profile = apex.player('atarfish')
        await message.channel.send('Apex Nick: ' + apex_profile.username + ' LvL: ' + apex_profile.level + ' Total Kills: ' + apex_profile.kills + ' Total Damage: ' + apex_profile.damage)

    elif '!help' in list_str:
        await message.channel.send('!rand- random list \n!flip- flip a coin\n!create- (!create player_name) - create a player \n!ka- (!ka player_name kills) - add kills to player\n!score- (!score player_name) - Player Kills\n!scb- ScoreBoard\n!rand_active- Random of active users\n!del- (!del player_name) - Delete player date\n!reset- (!reset play_name) - Reset kiils for player\n!reset_all- reset kills for all players \n!reset_db- reset data\n!stats- (!stats Apex_Username) - Get Total Apex stat\n!version - Get app version')

    elif '!version' in list_str:
        await message.channel.send('Version: 115')


client.run(token)