import nltk
from nltk.chat.util import Chat, reflections

pares = [
    [
        r"oi|ola|hey|hello",
        ["Ola","Oi","Hey!"]
    ],

    [
        r"Qual é o seu nome?",
        ["Meu nome é ChatBot","Eu sou o ChatBot!"]
    ],
    
    [
        r"Como está?|Como você está?|Como vai?",
        ["Estou bem, obrigado! E você?","Estou ótimo!"]
    ],

    [
        r"Tchau|Adeus|Bye|Bye Bye",
        ["Tchau","Até mais!"]
    ],
]

def chatbot():
  print("Olá, sou o ChatBot. Como posso ajuda-lo hoje?")
  chat = Chat(pares, reflections)

  while True:
    try:
        resposta = chat.respond(input())
        print(resposta)
    except KeyboardInterrupt:
        break
    
chatbot()