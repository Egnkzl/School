import time
import numpy as np
import sys



def delay_print(s):
    # One character at the time printing

    for c in s:
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(0.05)


class Pokemon:
    def __init__(self, name, types, moves, EVs, health='===================='):

        self.name = name
        self.types = types
        self.moves = moves
        self.attack = EVs['ATTACK']
        self.defense = EVs['DEFENSE']
        self.health = health
        self.bars = 20


    def fight(self, Pokemon2):


        # Fighting information

        print("-----POKEMONE BATTLE-----")
        print(f"\n{self.name}")
        print("TYPE/", self.types)
        print("ATTACK/", self.attack)
        print("DEFENSE/", self.defense)
        print("\nVS")

        print(f"\n{Pokemon2.name}")
        print("TYPE/", Pokemon2.types)
        print("ATTACK/", Pokemon2.attack)
        print("DEFENSE/", Pokemon2.defense)

        time.sleep(2)

        # Pokemon type advantages
        version = ['Fire', 'Water', 'Grass']
        for i,k in enumerate(version):
            if self.types == k:
                # Same type
                if Pokemon2.types == k:
                    string_1_attack = '\nIts not very effective...'
                    string_2_attack = '\nIts not very effective...'

                # Pokemon2 is stronger
                if Pokemon2.types == version[(i+1)%3]:
                    Pokemon2.attack *= 2
                    Pokemon2.defense *= 2
                    self.attack /= 2
                    self.defense /= 2
                    string_1_attack = '\nIts not very effective...'
                    string_2_attack = '\nIts super effective!'

                # Pokemon2 is weaker
                if Pokemon2.types == version[(i+2)%3]:
                    self.attack *= 2
                    self.defense *= 2
                    Pokemon2.attack /= 2
                    Pokemon2.defense /= 2
                    string_1_attack = '\nIts super effective!'
                    string_2_attack = '\nIts not very effective...'


        # Fight

        while (self.bars > 0) and (Pokemon2.bars > 0):

            print(f"\n{self.name}\t\tHLTH\t{self.health}")
            print(f"{Pokemon2.name}\t\tHLTH\t{Pokemon2.health}\n")

            print(f"Go {self.name}!")
            for i, x in enumerate(self.moves):
                print(f"{i+1}.", x)
            index = int(input('Pick a move: '))
            delay_print(f"\n{self.name} used {self.moves[index-1]}!")
            time.sleep(1)
            delay_print(string_1_attack)


            # Determine damage
            Pokemon2.bars -= self.attack
            Pokemon2.health = ""

            #  Defense boost
            for j in range(int(Pokemon2.bars+.1*Pokemon2.defense)):
                Pokemon2.health += "="

            time.sleep(1)
            print(f"\n{self.name}\t\tHLTH\t{self.health}")
            print(f"{Pokemon2.name}\t\tHLTH\t{Pokemon2.health}\n")
            time.sleep(.5)

            # Check if Pokemon fainted
            if Pokemon2.bars <= 0:
                delay_print("\n..." + Pokemon2.name + ' fainted.')
                break

            # Pokemon2s turn

            print(f"Go {Pokemon2.name}!")
            for i, x in enumerate(Pokemon2.moves):
                print(f"{i+1}.", x)
            index = int(input('Pick a move: '))
            delay_print(f"\n{Pokemon2.name} used {Pokemon2.moves[index-1]}!")
            time.sleep(1)
            delay_print(string_2_attack)

            # Determine damage
            self.bars -= Pokemon2.attack
            self.health = ""

            # Defense boost
            for j in range(int(self.bars+.1*self.defense)):
                self.health += "="

            time.sleep(1)
            print(f"{self.name}\t\tHLTH\t{self.health}")
            print(f"{Pokemon2.name}\t\tHLTH\t{Pokemon2.health}\n")
            time.sleep(.5)

            # Check to see if Pokemon fainted
            if self.bars <= 0:
                delay_print("\n..." + self.name + ' fainted.')
                break

        money = np.random.choice(1000)
        delay_print(f"\nOpponent paid you ${money}.\n")






if __name__ == '__main__':
    # Pokemons
    Charizard = Pokemon('Charizard', 'Fire', ['Flamethrower', 'Fly', 'Blast Burn', 'Fire Punch'], {'ATTACK':12, 'DEFENSE': 8})
    Blastoise = Pokemon('Blastoise', 'Water', ['Water Gun', 'Bubblebeam', 'Hydro Pump', 'Surf'],{'ATTACK': 10, 'DEFENSE':10})
    Venusaur = Pokemon('Venusaur', 'Grass', ['Vine Wip', 'Razor Leaf', 'Earthquake', 'Frenzy Plant'],{'ATTACK':8, 'DEFENSE':12})

    Charmander = Pokemon('Charmander', 'Fire', ['Ember', 'Scratch', 'Tackle', 'Fire Punch'],{'ATTACK':4, 'DEFENSE':2})
    Squirtle = Pokemon('Squirtle', 'Water', ['Bubblebeam', 'Tackle', 'Headbutt', 'Surf'],{'ATTACK': 3, 'DEFENSE':3})
    Bulbasaur = Pokemon('Bulbasaur', 'Grass', ['Vine Wip', 'Razor Leaf', 'Tackle', 'Leech Seed'],{'ATTACK':2, 'DEFENSE':4})

    Charmeleon = Pokemon('Charmeleon', 'Fire', ['Ember', 'Scratch', 'Flamethrower', 'Fire Punch'],{'ATTACK':6, 'DEFENSE':5})
    Wartortle = Pokemon('Wartortle', 'Water', ['Bubblebeam', 'Water Gun', 'Headbutt', 'Surf'],{'ATTACK': 5, 'DEFENSE':5})
    Ivysaur = Pokemon('Ivysaur\t', 'Grass', ['Vine Wip', 'Razor Leaf', 'Bullet Seed', 'Leech Seed'],{'ATTACK':4, 'DEFENSE':6})


    Charmander.fight(Squirtle)
