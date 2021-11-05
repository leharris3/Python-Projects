import random

def is_win(player, opponent):
    if (player == 'r' and opponent == 's') or (player == 's' and opponent == 'p') \
        or (player == 'p' and opponent == 'r'):
            return True
    else:
        return False

def rps():
    user = input("'r' for rock, 'p' for paper, 's' for scissors: ")
    computer = random.choice(['r', 'p', 's'])
    if user == computer:
        print ('tie')
    elif is_win(user, computer):
        print('you win')
    else:
        print('you lose')

rps();
     
