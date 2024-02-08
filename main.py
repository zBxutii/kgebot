import json, os
import discord
from discord.ext import commands
from discord.ext.commands import has_any_role


class Welcome_Embed():
  def __init__(self, member):
    # Member = nickname del nuevo usuario
    self.member = member

  @property
  def enviar(self):
    self.embed = discord.Embed(title=f'Bienvenido {self.member} Para unirte al servidor debes aceptar las siguientes reglas ... ', colour=int('DC75FF', 16))
    self.embed.add_field(name='Reglas:', value='1. Ser respetuoso. / 2. No usar lenguaje inapropiado. / 3. No hacer spam. / 4. No hacer flood.', inline=False)
    self.embed.add_field(name='Escribe el siguiente comando si estas de acuerdo:', value='.acepto', inline=False)
    return self.embed
    

client = commands.Bot(command_prefix = '.', intents = discord.Intents.all(), activity = discord.Game(name= 'By bautimiiranda'), help_command=None)
token = 'MTIwNDk0OTMyMzM5ODM4MTYyOQ.GbSgOl.TTzDTX63GYVYzJTzhvvV_QuhOAdzLxPwt-Dej8'

#Comandos
@client.command()
async def ping(ctx):
  await ctx.send('pong')

@client.command(name='acepto', help='Te agrega el rol de miembro')
async def add_user_role(ctx):
  if isinstance(ctx.channel, discord.channel.DMChannel):
    server =  client.get_guild(773634589863968829)
    rol = server.get_role(832093705191555123)
    member = server.get_member(ctx.message.author.id)
  await member.add_roles(rol)
  await ctx.author.send(f'Te has unido al servidor {server.name} correctamente!')
  
 #Eventos
@client.event
async def on_ready():
  print('Bot encendido')

@client.event
async def on_member_join(member):
  welcome_channel = client.get_channel(773634590937448490)
  welcome_embed = Welcome_Embed(member.name)
  await member.send(embed=welcome_embed.enviar)
  await welcome_channel.send(f'Bienvenido al servidor. {str(member.mention)}. Revisa tus mensajes privados para verificarte.')



client.run(token)
