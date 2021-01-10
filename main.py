import discord
import os
import requests
import json
import random
import urllib
from replit import db
from keep_alive import keep_alive

client = discord.Client()
awaitingQuestion = False
questionNumber = 0
subject = ""
section = ""

infile = open('HonoursScience20FH-Teller.txt', 'r')
allofit = infile.readlines()

# splitData = allofit[0].split("! SUBJECT ! ! SUBJECT ! !")
def question_list_Chemistry():
  global allofit
  splitData = allofit[0].split("! SUBJECT ! ! SUBJECT ! !")
  data = splitData
  data = data[0].split("! !")
  return data

def question_list_Physics():
  global allofit
  splitData = allofit[0].split("! SUBJECT ! ! SUBJECT ! !")
  data = splitData
  data = data[1].split("! !")
  return data

def question_list_Ecology():
  global allofit
  splitData = allofit[0].split("! SUBJECT ! ! SUBJECT ! !")
  data = splitData
  data = data[2].split("! !")
  return data

def question_list_Weather():
  global allofit
  splitData = allofit[0].split("! SUBJECT ! ! SUBJECT ! !")
  data = splitData
  data = data[3].split("! !")
  return data

def question_count():
  global allofit
  data = allofit
  data = data[0].split("! !")
  x = len(data)/2 - 6
  return str(x)

def get_question():
  global allofit
  global questionNumber
  data = allofit
  data = data[0].split("! !")
  print(len(data))
  n = random.randint(1, (len(data)/2))
  print(n)
  question = 2*n - 2
  questionNumber = question
  questionTxt = data[question]
  if questionTxt == " SUBJECT ":
    questionTxt = get_question()
  return(questionTxt)

def get_answer():
  global allofit
  data = allofit
  data = data[0].split("! !")
  global questionNumber
  answerTxt = data[questionNumber + 1]
  return(answerTxt)

def get_questionChem():
  global allofit
  global questionNumber
  splitData = allofit[0].split("! SUBJECT ! ! SUBJECT ! !")
  data = splitData
  data = data[0].split("! !")
  n = random.randint(1, (len(data)/2))
  question = 2*n - 2
  questionNumber = question
  questionTxt = data[question]
  return(questionTxt)

def get_answerChem():
  global allofit
  splitData = allofit[0].split("! SUBJECT ! ! SUBJECT ! !")
  data = splitData
  data = data[0].split("! !")
  global questionNumber
  answerTxt = data[questionNumber + 1]
  return(answerTxt)

def get_questionPhysics():
  global allofit
  global questionNumber
  splitData = allofit[0].split("! SUBJECT ! ! SUBJECT ! !")
  data = splitData
  data = data[1].split("! !")
  n = random.randint(1, (len(data)/2))
  question = 2*n - 2
  questionNumber = question
  questionTxt = data[question]
  return(questionTxt)

def get_answerPhysics():
  global allofit
  splitData = allofit[0].split("! SUBJECT ! ! SUBJECT ! !")
  data = splitData
  data = data[1].split("! !")
  global questionNumber
  answerTxt = data[questionNumber + 1]
  return(answerTxt)

def get_questionEcology():
  global allofit
  global questionNumber
  splitData = allofit[0].split("! SUBJECT ! ! SUBJECT ! !")
  data = splitData
  data = data[2].split("! !")
  n = random.randint(1, (len(data)/2))
  question = 2*n - 2
  questionNumber = question
  questionTxt = data[question]
  return(questionTxt)

def get_answerEcology():
  global allofit
  splitData = allofit[0].split("! SUBJECT ! ! SUBJECT ! !")
  data = splitData
  data = data[2].split("! !")
  global questionNumber
  answerTxt = data[questionNumber + 1]
  return(answerTxt)

def get_questionWeather():
  global allofit
  global questionNumber
  splitData = allofit[0].split("! SUBJECT ! ! SUBJECT ! !")
  data = splitData
  data = data[3].split("! !")
  n = random.randint(1, (len(data)/2))
  question = 2*n - 2
  questionNumber = question
  questionTxt = data[question]
  return(questionTxt)

def get_answerWeather():
  global allofit
  splitData = allofit[0].split("! SUBJECT ! ! SUBJECT ! !")
  data = splitData
  data = data[3].split("! !")
  global questionNumber
  answerTxt = data[questionNumber + 1]
  return(answerTxt)

def get_questionCARBONCYCLE():
  global allofit
  global questionNumber
  data = allofit
  data = data[0].split("! CARBONCYCLE ! ! CARBONCYCLE ! !")
  data = data[1].split("! !")
  print(data)
  n = random.randint(1, (len(data)/2))
  question = 2*n - 2
  questionNumber = question
  questionTxt = data[question]
  print(questionTxt + "hi")
  return(questionTxt)

def get_answerCARBONCYCLE():
  global allofit
  data = allofit
  data = data[0].split("! CARBONCYCLE ! ! CARBONCYCLE ! !")
  data = data[1].split("! !")
  global questionNumber
  answerTxt = data[questionNumber + 1]
  return(answerTxt) 


def get_quote():
  response = requests.get('https://zenquotes.io/api/random')
  json_data = json.loads(response.text)
  quote = json_data[0]['q'] + " -" + json_data[0]['a']
  return(quote)

@client.event
async def on_ready():
  print('We have logged in as {0.user}'.format(client))
  
@client.event
async def on_message(message):
  if message.author == client.user:
    return

  msg = message.content
  global awaitingQuestion
  global subject
  global section

  if awaitingQuestion == True:
    if msg.startswith('-check'):
      if subject == "chemistry":
        answer = get_answerChem()
        awaitingQuestion = False
        # subject = ""
        embed=discord.Embed(title="Answer:", description=answer ,color = 5483449)
        await message.channel.send(embed=embed)
      if subject == "physics":
        answer = get_answerPhysics()
        awaitingQuestion = False
        # subject = ""
        embed=discord.Embed(title="Answer:", description=answer ,color = 5483449)
        await message.channel.send(embed=embed)
      if subject == "ecology":
        answer = get_answerEcology()
        awaitingQuestion = False
        # subject = ""
        embed=discord.Embed(title="Answer:", description=answer ,color = 5483449)
        await message.channel.send(embed=embed)
      if subject == "weather":
        answer = get_answerWeather()
        awaitingQuestion = False
        # subject = ""
        embed=discord.Embed(title="Answer:", description=answer ,color = 5483449)
        await message.channel.send(embed=embed)
      if section == "carbon-cycle":
        answer = get_answerCARBONCYCLE()
        awaitingQuestion = False
        embed=discord.Embed(title="Answer:", description=answer ,color = 5483449)
        await message.channel.send(embed=embed)
      if subject == "":
        answer = get_answer()
        awaitingQuestion = False
        embed=discord.Embed(title="Answer:", description=answer ,color = 5483449)
        await message.channel.send(embed=embed)
    subject = ""
    section = ""

  if msg.startswith('$hello'):
    await message.channel.send('hi!')
  elif message.content.startswith('$inspire'):
    quote = get_quote()
    await message.channel.send(quote)
  elif msg.startswith('-quiz carboncycle'):
    question = get_questionCARBONCYCLE()
    subject = "none"
    section = "carbon-cycle"
    awaitingQuestion = True
    embed=discord.Embed(title="Question:", description=question ,color = 5483449)
    await message.channel.send(embed=embed)
  elif msg.startswith('-quiz c') or msg.startswith('-quiz chemistry'):
    question = get_questionChem()
    subject = "chemistry"
    awaitingQuestion = True
    embed=discord.Embed(title="Question:", description=question ,color = 5483449)
    await message.channel.send(embed=embed)
  elif msg.startswith('-quiz p') or msg.startswith('-quiz physics'):
    question = get_questionPhysics()
    subject = "physics"
    awaitingQuestion = True
    embed=discord.Embed(title="Question:", description=question ,color = 5483449)
    await message.channel.send(embed=embed)
  elif msg.startswith('-quiz e') or msg.startswith('-quiz ecology'):
    question = get_questionEcology()
    subject = "ecology"
    awaitingQuestion = True
    embed=discord.Embed(title="Question:", description=question ,color = 5483449)
    await message.channel.send(embed=embed)
  elif msg.startswith('-quiz w') or msg.startswith('-quiz weather'):
    question = get_questionWeather()
    subject = "weather"
    awaitingQuestion = True
    embed=discord.Embed(title="Question:", description=question ,color = 5483449)
    await message.channel.send(embed=embed)
  elif msg.startswith('-quiz'):
    question = get_question()
    awaitingQuestion = True
    subject = ""
    embed=discord.Embed(title="Question:", description=question ,color = 5483449)
    await message.channel.send(embed=embed)
  elif msg.startswith('-count'):
    count = question_count()
    await message.channel.send("Number of Questions:")
    await message.channel.send(count)
  elif msg.startswith('!oracle'):
    messages = msg.split(" ")  
    url = f"http://api.wolframalpha.com/v1/result?appid={os.getenv('WOLFRAMALPHA')}&i={messages[1]}"
    for m in range(2, len(messages)):
      url = url + "+" + str(messages[m])
    response = requests.get(url)
    if response.status_code == 501:
      await message.channel.send("Unable to process that query")
      return
    responseMessage = response.text
    await message.channel.send(responseMessage)

keep_alive()
client.run(os.getenv('TOKEN'))
