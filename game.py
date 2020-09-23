import random

winning_cases = {
    'water': ['scissors', 'fire', 'rock', 'hun', 'lightning', 'devil', 'dragon'],
    'dragon': ['snake', 'scissors', 'fire', 'rock', 'gun', 'lightning', 'devil'],
    'devil': ['tree', 'human', 'snake', 'scissors', 'fire', 'rock', 'gun'],
    'gun': ['wolf', 'tree', 'human', 'snake', 'scissors', 'fire', 'rock'],
    'rock': ['sponge', 'wolf', 'tree', 'human', 'snake', 'scissors', 'fire'],
    'fire': ['paper', 'sponge', 'wolf', 'tree', 'human', 'snake', 'scissors'],
    'scissors': ['air', 'paper', 'sponge', 'wolf', 'tree', 'human', 'snake'],
    'snake': ['water', 'air', 'paper', 'sponge', 'wolf', 'tree', 'human'],
    'human': ['dragon', 'water', 'air', 'paper', 'sponge', 'wolf', 'tree'],
    'tree': ['devil', 'dragon', 'water', 'air', 'paper', 'sponge', 'wolf'],
    'wolf': ['lightning', 'devil', 'dragon', 'water', 'air', 'paper', 'sponge'],
    'sponge': ['gun', 'lightning', 'devil', 'dragon', 'water', 'air', 'paper'],
    'paper': ['rock', 'gun', 'lightning', 'devil', 'dragon', 'water', 'air'],
    'air': ['fire', 'rock', 'gun', 'lightning', 'devil', 'dragon', 'water'],
    'lightning': ['tree', 'human', 'snake', 'scissors', 'fire', 'rock', 'gun']
}

default_options = ["rock", "paper", "scissors"]
options = []
scores = {}

with open("rating.txt", "r") as f:
    for line in f:
        score = line.split(" ")
        scores[score[0]] = score[1].split('\n')[0]


class User:
    choice = ""

    def set_choice(self, choice):
        self.choice = choice

    def get_choice(self):
        return self.choice


class Computer:
    choice = ""

    def set_choice(self, options_game):
        pick_choice = random.randint(0, len(options_game)-1)
        self.choice = options_game[pick_choice]

    def get_choice(self):
        return self.choice


def get_score(player):
    if player not in scores:
        scores[player] = str(0)


def print_score(rating):
    print("Your rating:", rating)


def is_draw(player1, player2):
    if player1 == player2:
        update_score(50)
        return True
    else:
        return False


def is_win(player1, player2):
    if player2 in winning_cases[player1]:
        update_score(100)
        return True
    else:
        return False


def update_score(n):
    scores[name] = str(int(scores[name]) + n)


player_1 = User()
player_2 = Computer()

print("Enter your name:", end=" ")
name = input()
print("Hello,", name)
get_score(name)
options = input().split(',')
if len(options) < 2:
    options = default_options
print("Okay, let's start")

while True:
    player_1.set_choice(input())
    if player_1.get_choice() == "!exit":
        print("Bye!")
        break
    elif player_1.get_choice() == "!rating":
        print_score(scores[name])
    elif player_1.get_choice() not in options:
        print("Invalid input")
    else:
        player_2.set_choice(options)
        if is_draw(player_1.get_choice(), player_2.get_choice()):
            print("There is a draw", player_2.get_choice())
        elif is_win(player_1.get_choice(), player_2.get_choice()):
            print("Well done. The computer chose " + player_2.get_choice())
        else:
            print("Sorry, but the computer chose " + player_2.get_choice())


with open("rating.txt", "w") as f:
    for k, v in scores.items():
        print(k, v, file=f)
