import json
import requests
import sys

pokemon_data = []
for id in range(1, 152): # non-inclusive range end
    response = requests.get("https://pokeapi.co/api/v2/pokemon/{}".format(id))

    if response.status_code != 200:
        print("Request failed")
        sys.exit()

    response_json = response.json()
    moves = []

    for move in response_json['moves']:
        for detail in move['version_group_details']:
            if detail['version_group']['name'] == 'red-blue':
                moves.append(move['move']['name'])

    pokemon_data.append({ "id": id, "name": response_json['name'], "moves": moves })

print(pokemon_data)

with open("./data/pokemon_data.json", 'w') as f:
    json.dump(pokemon_data, f)
