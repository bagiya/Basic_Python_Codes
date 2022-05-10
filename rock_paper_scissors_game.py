import random

# r > s, s > p, p > r

def play():
    user = input("Choose rock(r), paper(p),scissors(s): ")
    computer = random.choice(['r','p','s'])

    if user == computer:
        return "Tie game "

    if win(user,computer):
        return "User Won"
    return "User Lost"

def win(play_1,play_2):
    return (play_1 == 'r' and play_2 == 's') or (play_1 == 's' and play_2 == 'p') or (play_1 == 'p' and play_2 == 'r')

print(play())
