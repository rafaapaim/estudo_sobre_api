import requests
import json

request = requests.get('https://rickandmortyapi.com/api/character')
personagens = json.loads(request.text)

id = int(input("Digite o id (0-19): "))
print()

def retorna_personagem(id):
    personagem = personagens["results"][id]
    nome = personagem["name"]
    status = personagem["status"]
    especie = personagem["species"]
    tipo = personagem["type"]
    imagem = personagem["image"]
    origem = personagem["origin"]["name"]
    return "Nome: " + nome + "\nStatus: " + status + "\nEspecie: " + especie + "\nTipo: " + tipo + "\nOrigem: " + origem + "\nImagem: " + imagem

print(retorna_personagem(id))