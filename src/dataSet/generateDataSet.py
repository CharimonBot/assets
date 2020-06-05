import json
import requests as req
import math

def takeInput():
    print('-----------\n\n\n')
    print('What to generate:\n0) All\n1) /pokemon/\n2) /pokemon-species/\n3) /evolution-chain/\n4) /move/\n5) /ability/\nexit) Exit the program')
    print('\n\n\n-----------')
    return input()


def gPokemon():
    print('Generating /pokemon/')

    
def gPokemonSpecies():
    print('Generating /gPokemonSpecies/')

    
def gEvolutionChain():
    print('Generating /evolution-chain/')
    # Retrieve All Requests
    mainURL='https://pokeapi.co/api/v2/evolution-chain/?offset=0&limit=100000'
    print(mainURL)
    r=req.get(mainURL)
    data=r.json()
    # Storing Individual Requests
    URLs=[]
    results=[]
    count=0
    total=len(data['results'])
    for i in data['results']:
        count=count+1
        percent=math.floor((count/total)*100)
        if(percent%2==0):
            print(str(percent)+'% ('+str(count)+'/'+str(total)+')')
        url=i['url']
        URLs.append(i['url'])
        response=req.get(url)
        data=response.json()
        results.append(data)
    fileName='evolution-chain.json'
    with open(fileName,'w') as f:
        data={'evolution-chains':results}
        f.write(json.dumps(data))
        print('Data wrote to '+fileName)

    
def gMove():
    print('Generating /move/')

    
def gAbility():
    print('Generating /ability/')
    # Retrieve All Requests
    mainURL='https://pokeapi.co/api/v2/ability/?offset=0&limit=100000'
    print(mainURL)
    r=req.get(mainURL)
    data=r.json()
    # Storing Individual Requests
    URLs=[]
    results=[]
    count=0
    total=len(data['results'])
    for i in data['results']:
        count=count+1
        percent=math.floor((count/total)*100)
        if(percent%2==0):
            print(str(percent)+'% ('+str(count)+'/'+str(total)+')')
        url=i['url']
        URLs.append(i['url'])
        response=req.get(url)
        data=response.json()
        DataToWrite=dict()
        DataToWrite['id']=data['id']
        DataToWrite['is_main_series']=data['is_main_series']
        DataToWrite['name']=data['name']
        DataToWrite['generation']=data['generation']
        DataToWrite['flavor_text_entries']=[]
        DataToWrite['effect_entries']=[]
        for entry in data['flavor_text_entries']:
            if(entry['language']['name']=='en'):
                DataToWrite['flavor_text_entries'].append(entry)
        for entry in data['effect_entries']:
            if(entry['language']['name']=='en'):
                DataToWrite['effect_entries'].append(entry)
        results.append(DataToWrite)
    fileName='ability.json'
    with open(fileName,'w') as f:
        data={'abilities':results}
        f.write(json.dumps(data))
        print('Data wrote to '+fileName)

    

choice=takeInput()
while(choice!='exit'):
    if(choice=='0'):
        gPokemon()
        gPokemonSpecies()
        gEvolutionChain()
        gMove()
        gAbility()
    elif(choice=='1'):
        gPokemon()
    elif(choice=='2'):
        gPokemonSpecies()
    elif(choice=='3'):
        gEvolutionChain()
    elif(choice=='4'):
        gMove()
    elif(choice=='5'):
        gAbility()
    else:
        print('Enter 0,1,2,3,4,5 or exit')
    choice=takeInput()
    

    
