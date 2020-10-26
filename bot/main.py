from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer
import discord

class var:
    token = os.getenv("DISCORD_BOT_TOKEN")
bot = ChatBot('hi')
trainer = ChatterBotCorpusTrainer(bot)
client = discord.Client()
trainer.train(
    "chatterbot.corpus.english"
)
@client.event
async def on_ready():
    print(f'We have logged in as {client.user}')
    await client.change_presence(status = discord.Status.idle, activity = discord.Game("Listening to Music"))
@client.event
async def on_message(message):
    print(f"{message.channel}: {message.author}: {message.author.name}: {message.content}")
    if client.user.mentioned_in(message):
        msg = message.content
        msg = msg.split(' ', 1)[1]
        await message.channel.send(bot.get_response(msg))
client.run(var.token)
