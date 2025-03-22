import discord
#importar generador de contraseñas
from generador import gen_pass
from funciones import double_letter

# La variable intents almacena los privilegios del bot
intents = discord.Intents.default()
# Activar el privilegio de lectura de mensajes
intents.message_content = True
# Crear un bot en la variable cliente y transferirle los privilegios
client = discord.Client(intents=intents)

@client.event
async def on_ready():
    print(f'Hemos iniciado sesión como {client.user}')

@client.event
async def on_message(message):
    if message.author == client.user:
        return
    if message.content.startswith('$hello'):
        await message.channel.send("Hi!")
    elif message.content.startswith('$bye'):
        await message.channel.send("\U0001f642")
    elif message.content.startswith('pass'):
        await message.channel.send(gen_pass(10))
    elif message.content.startswith('2letter'):
        await message.channel.send(double_letter)
    else:
        await message.channel.send(message.content)
client.run(tu token aqui)
