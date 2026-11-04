import requests

def main():
    #Make an API request to the D&D 5th Edition API for all spell data
    url = "https://www.dnd5eapi.co/api/2014/spells"
    headers = {'Accept': 'application/json'}
    response = requests.get(url, headers=headers)

    #Check for successful request, load spell data into variable
    if response.status_code == 200:
        spells_data = response.json()
        spells = spells_data['results']

        print("\nD&D 5th Edition Spell Encyclopedia")
        print("Search for spells by their level, then see what they do!\n")


        spell_list = []
        while True:
            try:
                #Accept input as spell level 1 through 9
                spell_level = int(input("Enter spell level (1 - 9): "))
                valid_levels = list(range(1, 10))
                print()

                #Output a list of spells in four columns
                while True:
                    if spell_level in valid_levels:
                        for spell in spells:
                            if spell['level'] == spell_level:
                                spell_list.append(spell['name'])
                        for i in range(0, len(spell_list), 4):
                            print(' \\ '.join(spell_list[i:i + 4]))
                        print()
                        break
                    #Out of range error
                    else:
                        spell_level = int(input("Out of range. Valid spell levels are 1 - 9: "))
                        print()
                break
            #Non-int error
            except ValueError:
                print("\nEnter a spell level between 1 and 9.\n")
    else:
        #Data retrieval error
        print("There was an error while trying to retrieve data.")
        exit(1)

    #Accept input as name of spell, search for spell in json
    while True:
        found = False
        query = input("Type the name of the spell you'd like to learn about: ").lower()
        for spell in spells:
            if query == spell['name'].lower():
                chosen_spell = spell['index']
                found = True
        if found:
            break
        #Invalid spell name error
        else:
            print("\nSpell not found, please try again.\n")

    #API request for specific spell data
    url2 = f"https://www.dnd5eapi.co/api/2014/spells/{chosen_spell}"
    payload = {}
    response2 = requests.request("GET", url2, headers=headers, data=payload)

    #Check for successful request, retrieve chosen spell description
    if response2.status_code == 200:
        chosen_spell_data = response2.json()
        print()
        print(' '.join(chosen_spell_data['desc']))
    else:
        #Data retrieval error
        print("There was an error while trying to retrieve data.")
        exit(1)

if __name__ == "__main__":
    main()