import discord

intents = discord.Intents.default()
intents.message_content = True

client = discord.Client(intents=intents)

@client.event
async def on_ready():
    print(f"Conectado como {client.user}")

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content == "haces mi parte?":
        await message.channel.send("nunca hare tu parte brother")

client.run("YOUR TOKEN")
