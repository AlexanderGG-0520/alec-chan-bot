import discord
from discord import app_commands
from random import randrange as rr
import asyncio

TOKEN = "MTIwNjExMTI2MjMwODU2NTA1Mg.G2IPis.M0KeFCgcKdK78kKoej9WBh2ZkFVzXatKquy0Y4"

activity = discord.Activity(name="起動中…", type=discord.ActivityType.playing)
intents = discord.Intents.all()
client = discord.Client(intents=intents, activity=activity)
tree = app_commands.CommandTree(client)


@client.event
async def on_ready():
    print("起動完了")
    try:
     synced = await tree.sync()
     print(f"{len(synced)}個のコマンドを同期しました")
    except Exception as e:
     print(e)
    
    #15秒毎にアクティヴィティを更新します
    while True:
       await client.change_presence(activity = discord.Activity(name="Help:!help", type=discord.ActivityType.playing))
       await asyncio.sleep(15)
       joinserver=len(client.guilds)
       servers=str(joinserver)
       await client.change_presence(activity = discord.Activity(name="サーバー数:"+servers, type=discord.ActivityType.playing))
       await asyncio.sleep(15)
       await client.change_presence(activity = discord.Activity(name="乱数:"+str(rr(0,101)), type=discord.ActivityType.playing))
       await asyncio.sleep(15)
    

#テストコマンドを定義します
@tree.command(name="test",description="テストコマンドです。")
async def test_command(interaction: discord.Interaction):
    await interaction.response.send_message("てすと！",ephemeral=True)#ephemeral=True→「これらはあなただけに表示されています」

#メッセージ検索のコマンドを定義します
@tree.command(name="search", description="自身や他人のUIDやVALORANTのパーティコードを検索します。")
async def search_command(interaction: discord.Interaction, channel:discord.TextChannel, member:discord.Member):
  print(channel.id, member.id)
  channel_id = channel.id
  member_id = member.id
  async for message in channel.history(limit=None):
    if message.author.id == member_id:
      content = message.content
      print(content)
      await interaction.response.send_message(f"{member}, {content}", ephemeral=False)

client.run(TOKEN)