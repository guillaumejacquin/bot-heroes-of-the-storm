import discord
from discord.ext import commands
import urllib.request
import os

bot = commands.Bot(command_prefix =".", description = "yolo")

@bot.event
async def on_ready():
    print("prêt!")

@bot.command()
async def coucou(ctx):
    await ctx.send("yo c est le test")


    
@bot.command()
@commands.has_permissions(kick_members = True)
async def clear(ctx, nombre):
    try:
        nombre_int = int(nombre)
        messages = await ctx.channel.history(limit = nombre_int + 1).flatten()
        for message in messages:
            await message.delete()  
        mess = "Cleared **" + str(nombre_int) + "** message(s)."
        await ctx.send(mess)
    except:
        await ctx.send("fuck off, its not a number")

@bot.command()
async def test(ctx, *heroes):
    heroes = " ".join(heroes)
    print(heroes)

@bot.command()
async def info(ctx, *heroes):
    heroes = " ".join(heroes)
    heroes = heroes.lower()
    heroes = heroes.capitalize()
    with urllib.request.urlopen("https://www.heroesprofile.com/Global/Hero/") as response:
        texte = response.read()
        poste_string = str(texte)
        splitted = poste_string.split()
        texte = False
        access = False

        heroess = heroes.replace("'", "\\'")
        heroess = heroes.replace("ù", "\\xc3\\xba")
        print(heroes)

        if (heroes == "Li-ming"):
            heroess = "Ming"
        
        if (heroes == "D.va"):
            heroess = "D.Va"
        if (heroes == "Sgt.hammer"):
            heroess = "Sgt."


        i = 0
        j = 0
        winrate = ""
        popularity = ""
        pick_rate = ""
        ban_rate = ""
        game_played = ""
        k = 0
        z = 0
        y = 0
        d = 0
        
        for word in splitted:
            if (heroess in word) or (access):
                i += 1
                if (i >= 8):
                    access = True
                    if("win_rate_cell" in word):
                        j += 1
                        if (j == 1):
                            elmts = word.split('>')
                            winrate = elmts[1]
                            winrate = winrate.split('<')
                            winrate = winrate[0]
                    if("popularity_cell" in word):
                        k += 1
                        if (k == 1):
                            elmts = word.split('>')
                            popularity = elmts[1]
                            popularity = popularity.split('<')
                            popularity = popularity[0]
                    if("pick_rate_cell" in word):
                        z += 1
                        if (z == 1):
                            elmts = word.split('>')
                            pick_rate = elmts[1]
                            pick_rate = pick_rate.split('<')
                            pick_rate = pick_rate[0]
                    if("ban_rate" in word):
                        y += 1
                        if (y == 1):
                            elmts = word.split('>')
                            ban_rate = elmts[1]
                            ban_rate = ban_rate.split('<')
                            ban_rate = ban_rate[0]
                    if("games_played_cell" in word):
                        d += 1
                        if (d == 1):
                            elmts = word.split('>')
                            game_played = elmts[1]
                            game_played = game_played.split('<')
                            game_played = game_played[0]
    image = "https://raw.githubusercontent.com/HeroesToolChest/heroes-images/master/heroesimages/heroportraits/storm_ui_glues_draft_portrait_"
    image2 = heroes.lower()
    image3 = ".png"
    image = image + image2+ image3
    embed = discord.Embed(title = heroes, color=0x2C75FF)
    embed.set_thumbnail(url= image)
    embed.add_field(name = "Winrate", value = winrate, inline = False)
    embed.add_field(name = "Popularity", value = popularity, inline = False)
    embed.add_field(name = "Pick rate", value = pick_rate, inline = False)
    embed.add_field(name = "Ban rate", value = ban_rate, inline = False)
    embed.add_field(name = "Game played", value = game_played, inline = False)
    await ctx.channel.send(embed=embed)


token = os.getenv('TOKEN')
bot.run(token)