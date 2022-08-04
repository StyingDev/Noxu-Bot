import discord
from discord.ext import commands
from discord.ext import tasks
import random
from discord.utils import get
from random import choice
import praw
from PIL import Image
from io import BytesIO
import json
import os
import asyncio
import requests
import time
import datetime





timezone = time.time()
local_time = time.ctime(timezone)

intents = discord.Intents.all()
intents.members = True

client = commands.Bot(command_prefix=">", case_insensitive=True, intents = intents)
client.remove_command('help')




@client.event
async def on_ready():
    print(local_time)
    print("Bot Started.")
    change_status.start()






@tasks.loop(seconds=20)
async def change_status():
    status = [f"On {len(client.guilds)} Server|>help", "with Your Hopes And Dreams", f"Update 1.2.1", ">help"]
    await client.change_presence(activity=discord.Game(choice(status)))

#------------------------------------------------------------------------------------------------------------------------------------------
#User Commands Below









#testing Room Below
#--------------------------------------------------


#add ur id ig?


@client.event
async def is_owner(ctx):
    return ctx.author.id == 418425400625070090
@client.command()
@commands.check(is_owner)
async def rickroll(ctx, member : discord.Member):
    await ctx.send(f"https://tenor.com/7jGZ.gif {member.mention}")
@rickroll.error
async def rickroll_error(ctx, error):
    if isinstance(error, commands.CheckFailure):
        await ctx.send ('You Are Not Worthy')




#testing Room End
#----------------------------------------------------------------------------------------
#help command i had to do it again :C

@client.group(invoke_without_command=True, case_insensitive=True)
async def help(ctx):
    emlol = discord.Embed(title = "***Help***", description = "***Use >help <Command> For Extended Information***", color = ctx.author.color)

    emlol.add_field(name = "Moderation", value = "Kick/Ban/Clear/Unban/whois",inline=False)
    emlol.add_field(name = "Fun", value = "8ball/Meme/quote/treat/Picture",inline=False)
    emlol.add_field(name = "informational", value = "ChangeLog/Ping/Credits/avatar",inline=False)
    emlol.add_field(name = "Giveawaying", value = "Giveaway/reroll",inline=False)


    emlol.set_footer(icon_url = ctx.author.avatar_url, text = f"Requested By {ctx.author.name}")

    await ctx.send(embed = emlol)



@help.command()
async def kick(ctx):
    emlol = discord.Embed(title = "Help", description = "Kick An Member From Guild", color = ctx.author.color)

    emlol.add_field(name = "**Syntax**" , value = ">Kick <Member> [Reason]")

    emlol.set_footer(icon_url = ctx.author.avatar_url, text = f"Requested By {ctx.author.name}")

    await ctx.send(embed = emlol)



@help.command()
async def ban(ctx):
    emlol = discord.Embed(title = "Help", description = "Bans An Member From Guild", color = ctx.author.color)

    emlol.add_field(name = "**Syntax**" , value = ">ban <Member> [Reason]")

    emlol.set_footer(icon_url = ctx.author.avatar_url, text = f"Requested By {ctx.author.name}")

    await ctx.send(embed = emlol)



@help.command()
async def clear(ctx):
    emlol = discord.Embed(title = "Help", description = "Clears certain ammount of Messages from chat", color = ctx.author.color)

    emlol.add_field(name = "**Syntax**" , value = ">clear [Amount of messages to delete]")

    emlol.set_footer(icon_url = ctx.author.avatar_url, text = f"Requested By {ctx.author.name}")

    await ctx.send(embed = emlol)



@help.command()
async def unban(ctx):
    emlol = discord.Embed(title = "Help", description = "unban An Member From Guild", color = ctx.author.color)

    emlol.add_field(name = "**Syntax**" , value = ">unban <User#id>")

    emlol.set_footer(icon_url = ctx.author.avatar_url, text = f"Requested By {ctx.author.name}")

    await ctx.send(embed = emlol)



@help.command()
async def whois(ctx):
    emlol = discord.Embed(title = "Help", description = "Kick An Member From Guild", color = ctx.author.color)

    emlol.add_field(name = "**Syntax**" , value = ">whois <Member>")

    emlol.set_footer(icon_url = ctx.author.avatar_url, text = f"Requested By {ctx.author.name}")

    await ctx.send(embed = emlol)



@help.command(aliases=["8ball"])
async def _8ball(ctx):
    emlol = discord.Embed(title = "Help", description = "contemplate Your life decisions", color = ctx.author.color)

    emlol.add_field(name = "**Syntax**" , value = ">8ball <question>")

    emlol.set_footer(icon_url = ctx.author.avatar_url, text = f"Requested By {ctx.author.name}")

    await ctx.send(embed = emlol)



@help.command()
async def meme(ctx):
    emlol = discord.Embed(title = "Help", description = "Shows Meme (Sometimes May not work)", color = ctx.author.color)

    emlol.add_field(name = "**Syntax**" , value = ">meme")

    emlol.set_footer(icon_url = ctx.author.avatar_url, text = f"Requested By {ctx.author.name}")

    await ctx.send(embed = emlol)


@help.command()
async def ping(ctx):
    emlol = discord.Embed(title = "Help", description = "Shows Bots latency", color = ctx.author.color)

    emlol.add_field(name = "**Syntax**" , value = ">ping")

    emlol.set_footer(icon_url = ctx.author.avatar_url, text = f"Requested By {ctx.author.name}")

    await ctx.send(embed = emlol)



@help.command()
async def picture(ctx):
    emlol = discord.Embed(title = "Help", description = "Picture Manupliation", color = ctx.author.color)

    emlol.add_field(name = "**Syntax**" , value = ">picture(for More Commands)")

    emlol.set_footer(icon_url = ctx.author.avatar_url, text = f"Requested By {ctx.author.name}")

    await ctx.send(embed = emlol)





@help.command()
async def changelog(ctx):
    emlol = discord.Embed(title = "Help", description = "Show Changes Made", color = ctx.author.color)

    emlol.add_field(name = "**Syntax**" , value = ">ChangeLog")

    emlol.set_footer(icon_url = ctx.author.avatar_url, text = f"Requested By {ctx.author.name}")

    await ctx.send(embed = emlol)



@help.command()
async def credit(ctx):
    emlol = discord.Embed(title = "Help", description = "Credits", color = ctx.author.color)

    emlol.add_field(name = "**Syntax**" , value = ">credit")

    emlol.set_footer(icon_url = ctx.author.avatar_url, text = f"Requested By {ctx.author.name}")

    await ctx.send(embed = emlol)




@help.command()
async def quote(ctx):
    emlol = discord.Embed(title = "Help", description = "Shows Famous Quote", color = ctx.author.color)

    emlol.add_field(name = "**Syntax**" , value = ">quote")

    emlol.set_footer(icon_url = ctx.author.avatar_url, text = f"Requested By {ctx.author.name}")

    await ctx.send(embed = emlol)





@help.command()
async def avatar(ctx):
    emlol = discord.Embed(title = "Help", description = "Shows Users Profile Picture", color = ctx.author.color)

    emlol.add_field(name = "**Syntax**" , value = ">avatar <@user>")

    emlol.set_footer(icon_url = ctx.author.avatar_url, text = f"Requested By {ctx.author.name}")

    await ctx.send(embed = emlol)




@help.command()
async def Treat(ctx):
    emlol = discord.Embed(title = "Help", description = "Treat A User", color = ctx.author.color)

    emlol.add_field(name = "**Syntax**" , value = ">Treat <Name>")

    emlol.set_footer(icon_url = ctx.author.avatar_url, text = f"Requested By {ctx.author.name}")

    await ctx.send(embed = emlol)




@help.command()
async def Giveaway(ctx):
    emlol = discord.Embed(title = "Help", description = "Host a Giveaway", color = ctx.author.color)

    emlol.add_field(name = "**Syntax**" , value = ">Giveaway")

    emlol.set_footer(icon_url = ctx.author.avatar_url, text = f"Requested By {ctx.author.name}")

    await ctx.send(embed = emlol)




@help.command()
async def reroll(ctx):
    emlol = discord.Embed(title = "Help", description = "reroll a Giveaway", color = ctx.author.color)

    emlol.add_field(name = "**Syntax**" , value = ">reroll <#Text-channel> <id of the Giveaway Message> ")

    emlol.set_footer(icon_url = ctx.author.avatar_url, text = f"Requested By {ctx.author.name}")

    await ctx.send(embed = emlol)



#----------------------------------------------------------------------------------------------------------------------

































#changelog
@client.command()
async def changelog(ctx):
    change = discord.Embed(title = "ChangeLog", description = "Updates Made To Noxu Bot",color = ctx.author.color)

    change.add_field(name = "1.2.1", value = "Added new image to picture manupilation")

    change.add_field(name = "1.2.0", value = "Added Giveaway")

    change.add_field(name = "1.1.9", value = "Removed leveling system(reason its just not good with out a DB")

    change.add_field(name = "1.1.8", value = "Added >avatar Command")

    change.add_field(name = "1.1.7", value = "Made >whois Better")

    change.add_field(name = "1.1.6", value = "Added >treat Command")

    change.add_field(name = "1.1.5", value = "Minor improvements")

    change.add_field(name = "1.1.4", value = "Added >quote Command")

    change.add_field(name = "1.1.3", value = "Added Credits")

    change.add_field(name = "1.1.2", value = "Made >Picture Command Better")

    change.add_field(name = "1.1.1", value = "Added changelog Feature ")

    change.add_field(name = "1.1.0", value = "Added Define Feature ")

    change.add_field(name = "1.0.9", value = "Custom Help Command ")

    

    change.set_footer(icon_url = ctx.author.avatar_url, text = f"Requested By {ctx.author.name}")

    await ctx.send(embed = change)


#quote Command

@client.command()
async def quote(ctx):
    results = requests.get("https://type.fit/api/quotes").json()
    numbelol = random.randint(1, 1500)
    content = discord.Embed(title=results[numbelol]["text"],description="",color = ctx.author.color)
    await ctx.send(embed=content)



def convert(time):
    pos = ["s","m","h","d"]

    time_dict = {"s" : 1, "m" : 60, "h" : 3600 , "d" : 3600*24}

    unit = time[-1]

    if unit not in pos:
        return -1
    try:
        val = int(time[:-1])
    except:
        return -2


    return val * time_dict[unit]


@client.command()
@commands.has_role("Giveaways")
async def giveaway(ctx):
    await ctx.send("Let's start with this giveaway! Answer these questions within 15 seconds!")

    questions = ["Which channel should it be hosted in?", 
                "What should be the duration of the giveaway? (s|m|h|d)",
                "What is the prize of the giveaway?"]

    answers = []

    def check(m):
        return m.author == ctx.author and m.channel == ctx.channel 

    for i in questions:
        await ctx.send(i)

        try:
            msg = await client.wait_for('message', timeout=15.0, check=check)
        except asyncio.TimeoutError:
            await ctx.send('You didn\'t answer in time, please be quicker next time!')
            return
        else:
            answers.append(msg.content)
    try:
        c_id = int(answers[0][2:-1])
    except:
        await ctx.send(f"You didn't mention a channel properly. Do it like this {ctx.channel.mention} next time.")
        return

    channel = client.get_channel(c_id)

    time = convert(answers[1])
    if time == -1:
        await ctx.send(f"You didn't answer the time with a proper unit. Use (s|m|h|d) next time!")
        return
    elif time == -2:
        await ctx.send(f"The time must be an integer. Please enter an integer next time")
        return            

    prize = answers[2]

    await ctx.send(f"The Giveaway will be in {channel.mention} and will last {answers[1]}!")


    embed = discord.Embed(title = "Giveaway!", description = f"{prize}", color = ctx.author.color)

    embed.add_field(name = "Hosted by:", value = ctx.author.mention)

    embed.set_footer(text = f"Ends {answers[1]} from now!")

    my_msg = await channel.send(embed = embed)


    await my_msg.add_reaction("🎉")


    await asyncio.sleep(time)


    new_msg = await channel.fetch_message(my_msg.id)


    users = await new_msg.reactions[0].users().flatten()
    users.pop(users.index(client.user))

    winner = random.choice(users)

    await channel.send(f"Congratulations! {winner.mention} won {prize}!")


@client.command()
@commands.has_role("Giveaways")
async def reroll(ctx, channel : discord.TextChannel, id_ : int):
    try:
        new_msg = await channel.fetch_message(id_)
    except:
        await ctx.send("The id was entered incorrectly.")
        return
    
    users = await new_msg.reactions[0].users().flatten()
    users.pop(users.index(client.user))

    winner = random.choice(users)

    await channel.send(f"Congratulations! The new winner is {winner.mention}.!")    



@giveaway.error
async def giveaway_error(ctx, error):
    if isinstance(error, commands.MissingRole):
        await ctx.send ('Missing Role "Giveaways"')




#Invite Bots
@client.command()
async def credits(ctx):
    creditslol = discord.Embed(title = "Credits",description = "Bot Made By Drizzy Stying#1472",color = ctx.author.color)
    creditslol.add_field(name = "Invite Bot",value="https://discord.com/oauth2/authorize?client_id=648798358219128853&permissions=8&scope=bot")
    creditslol.add_field(name = "Bot Support Server" , value = "https://discord.gg/hj3B4TJ")

    await ctx.send(embed=creditslol)






@client.command(case_insensitive=True)
async def treat(ctx, member:discord.Member):
    if member == ctx.author:
        await ctx.send("You can't treat youself!")
        return
    embed=discord.Embed(
        description=f'You offered {member.name} a treat! {member.mention} react to the emoji below to accept!',
        color=0x006400
    )
    timeout=int(15.0)
    message = await ctx.channel.send(embed=embed)

    await message.add_reaction('🍫')

    def check(reaction, user):
        return user == member and str(reaction.emoji) == '🍫'

    try:
        reaction, user = await client.wait_for('reaction_add', timeout=timeout, check=check)

    except asyncio.TimeoutError:
        msg=(f"{member.mention} didn't accept the treat in time!!")
        await ctx.channel.send(msg)

    else:
        await ctx.channel.send(f"{member.mention} You have accepted {ctx.author.name}'s offer!")





@client.command()
async def Picture(ctx):
    pichelp = discord.Embed(title="Picture Manupiution",description="Makes Mentioned User In an Scenario", color = ctx.author.color)
    pichelp.add_field(name=">Samurai",value="Makes Samurai Image Of User")
    pichelp.add_field(name=">Speech",value="Makes An Person Give a Speech")
    pichelp.add_field(name=">Wanted",value="Makes An Person Wanted For 100$ :joy:")
    pichelp.add_field(name=">grave",value="Rip :'(")
    pichelp.add_field(name=">Donkey",value="Donkey Lol")
    pichelp.add_field(name=">returntomonke",value="Reject Humanity")


    await ctx.send(embed=pichelp)


@client.command(aliases=["avatar"])
async def pfp(ctx, member: discord.Member):
    embed = discord.Embed(title=f"{member.name}'s avatar")
    embed.set_image(url=member.avatar_url)
    await ctx.send(embed=embed)


#Picture Manupiution (start)

#Wanted Poster
@client.command()
async def wanted(ctx, user: discord.Member = None):
    if user == None:
        user = ctx.author

    wanted = Image.open("wanted.jpg")

    asset = user.avatar_url_as(size = 128)

    data = BytesIO(await asset.read())

    pfp = Image.open(data)
    pfp = pfp.resize((78,78))

    wanted.paste(pfp, (54,95))

    wanted.save("profile.jpg")

    await ctx.send(file = discord.File("profile.jpg"))



@client.command()
async def samurai(ctx, user: discord.Member = None):
    if user == None:
        user = ctx.author

    samurai = Image.open("samurai.jpg")

    asset = user.avatar_url_as(size = 128)

    data = BytesIO(await asset.read())

    pfp = Image.open(data)
    pfp = pfp.resize((166,186))

    samurai.paste(pfp, (127,65))

    samurai.save("profile2.jpg")

    await ctx.send(file = discord.File("profile2.jpg"))



#speech Pictures
@client.command()
async def speech(ctx, user: discord.Member = None):
    if user == None:
        user = ctx.author

    speech = Image.open("speech.jpg")

    asset = user.avatar_url_as(size = 128)

    data = BytesIO(await asset.read())

    pfp = Image.open(data)
    pfp = pfp.resize((78,78))

    speech.paste(pfp, (155,55))

    speech.save("profile1.jpg")

    await ctx.send(file = discord.File("profile1.jpg"))

@client.command()
async def grave(ctx, user: discord.Member = None):
    if user == None:
        user = ctx.author

    grave = Image.open("grave.jpg")

    asset = user.avatar_url_as(size = 128)

    data = BytesIO(await asset.read())

    pfp = Image.open(data)
    pfp = pfp.resize((63,53))

    grave.paste(pfp, (109,68))

    grave.save("grave1.jpg")

    await ctx.send(file = discord.File("grave1.jpg"))


@client.command()
async def returntomonke(ctx, user: discord.Member = None):
    if user == None:
        user = ctx.author

    monke = Image.open("monke.jpg")

    asset = user.avatar_url_as(size = 128)

    data = BytesIO(await asset.read())

    pfp = Image.open(data)
    pfp = pfp.resize((100,100))

    monke.paste(pfp, (190,52))

    monke.save("monke1.jpg")

    await ctx.send(file = discord.File("monke1.jpg"))







@client.command()
async def donkey(ctx, user: discord.Member = None):
    if user == None:
        user = ctx.author

    donkey = Image.open("donkey.jpg")

    asset = user.avatar_url_as(size = 128)

    data = BytesIO(await asset.read())

    pfp = Image.open(data)
    pfp = pfp.resize((223,234))

    donkey.paste(pfp, (421,285))

    donkey.save("donkey1.jpg")

    await ctx.send(file = discord.File("donkey1.jpg"))






#picture manupliaton (end)





#Ping Command 
@client.command()
async def ping(ctx):
    pingembed = discord.Embed(title = "Ping", description = f"Pong! {round(client.latency * 1000)}ms", color = ctx.author.color)
    await ctx.send(embed=pingembed)






#8Ball Command
@client.command(aliases=["8ball"])
async def  _8ball(ctx, *, question):
    responses = ["It is certain.",
                "It is decidedly so.",
                "Without a doubt.",
                "Yes - definitely.",
                "You may rely on it.",
                "As I see it, yes.",
                "Most likely.",
                "Outlook good.",
                "Yes.",
                "Signs point to yes.",
                "Reply hazy, try again.",
                "Ask again later.",
                "Better not tell you now.",
                "Cannot predict now.",
                "Concentrate and ask again.",
                "Don't count on it.",
                "My reply is no.",
                "My sources say no.",
                "Outlook not so good.",
                "Very doubtful."]



    e8ball = discord.Embed(title = "8ball",description = f"Question: {question}\nAnswer: {random.choice(responses)}", color = ctx.author.color)



    await ctx.send(embed=e8ball)

#













#Connects To Reddit api 
#add ur info or no work
reddit = praw.Reddit(client_id = "",
                     client_secret = "",
                     username = "",
                     password = "",
                     user_agent = "praw" )



#Reddit Meme Command
@client.command()
async def meme(ctx):
    subreddit = reddit.subreddit("dankmemes")

    all_subs = []

    top = subreddit.top(limit = 300)


    for submission in top:
        all_subs.append(submission)

    random_sub = random.choice(all_subs)

    name = random_sub.title
    url = random_sub.url

    em = discord.Embed(title = name)
    em.set_image(url = url)

    await ctx.send(embed = em)




#user Commands Above
#---------------------------------------------------------------------------------------
#moderation Commands Below





#Whois command (Gives Information Of Mentioned User)



@client.command(aliases = ["userinfo", "aboutuser"])
async def whois(ctx, member : discord.Member = None):
    member = ctx.author if not member else member
    roles = [role for role in member.roles]
    LOLOO = discord.Embed(colour=member.colour, timestamp=ctx.message.created_at)
    LOLOO.set_author(name=f"User info - {member}")
    LOLOO.set_thumbnail(url=member.avatar_url)
    LOLOO.set_footer(text=f"Requested by {ctx.author}", icon_url=ctx.author.avatar_url)
    LOLOO.add_field(name="ID: ", value=member.id, inline=True)
    LOLOO.add_field(name="Created account at: ", value=member.created_at.strftime("%a, %d %#B %Y, %I:%M %p UTC"))
    LOLOO.add_field(name="Joined server at: ", value=member.joined_at.strftime("%a, %d %#B %Y, %I:%M %p UTC"))
    LOLOO.add_field(name=f"Roles ({len(roles)})", value=" ".join([role.mention for role in roles]), inline=True)
    LOLOO.add_field(name="Top role:", value=member.top_role.mention, inline=True)
    LOLOO.add_field(name="Bot? ", value=member.bot, inline=True)
    await ctx.send(embed=LOLOO)





#clear Command (clears Chat If No Number Told Delets 5 Messages (default)
@client.command()
@commands.has_permissions(manage_messages=True)
async def clear(ctx, ammount=5):
    await ctx.channel.purge(limit=ammount)

#kick Command (kicks mentioned User From Server)
@client.command()
@commands.has_permissions(kick_members=True, administrator=True)
async def kick(ctx, member : discord.Member, *, reason=None):
    await member.kick(reason=reason)

#ban Command (Bans Mentioned User From Server)



@client.command()
@commands.has_permissions(ban_members=True, administrator=True)
async def ban(ctx, member : discord.Member, *, reason=None):
    await member.ban(reason=reason)






#unban Command (unbanns User In (User#1234) Format)




@client.command()
@commands.has_permissions(ban_members=True, administrator=True)
async def unban(ctx, *, member):
    banned_users = await ctx.guild.bans()
    member_name, member_discriminator = member.split("#")

    for ban_entry in banned_users:
        user = ban_entry.user

        if (user.name, user.discriminator) == (member_name, member_discriminator):
            await ctx.guild.unban(user)
            unbanmsg = discord.Embed(title = "Unbanned", description = f"{user.mention}")
            await ctx.send(embed=unbanmsg)
            return


#Moderation Commands Above
#----------------------------------------------------------------------------------------------------------





#token add
client.run("token is here")
