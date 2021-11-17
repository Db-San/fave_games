import os
import pickle

### Favorite Games ###
# Write a terminal app that asks people for their favorite games.

### Functions ###

def dislay_title_bar():
    os.system('clear')
    print('-------------------------------------------')
    print('--- Favorite Games --- Stored (%d) ---' % len(fave_games))
    print('-------------------------------------------') 

def get_choice():
    print('\nActions:')
    print('[1] See all stored games.')
    print('[2] Enter a new game.')
    print('[q] Quit.')
    choice = input('-> ')  
    return choice

def get_new_game():
    print('Enter a new game:')
    new_game = input('-> ')
    new_game = new_game.lower()
    if new_game in fave_games:
        dislay_title_bar()
        print('-> %s' % new_game.title())
        print('I know that game, and I like it too.')
    else:
        fave_games.append(new_game)
        dislay_title_bar()
        print('-> %s' % new_game.title())
        print('This game is new to me, and I want to learn more.')

def show_games():
    print('Currently stored games:')
    for index, game in enumerate(fave_games):
        game = game.title()
        index += 1
        print('#%d - %s' % (index, game))

def quit():
    try:
        file_object = open('favegames.pydata', 'wb')
        pickle.dump(fave_games, file_object)
        file_object.close()
        print('Thank you for playing! I will remember these games.')
    except Exception as e:
        print('Thank you for playing! I will not be able to remember these games.')    
        print(e)

def load_games():
    fave_games = []
    try:
        file_object = open('favegames.pydata', 'rb')
        fave_games = pickle.load(file_object)
        file_object.close()
        return fave_games
    except Exception as e:
        print(e)
        return fave_games

### Main Program ###

choice = ' '
fave_games = load_games()
dislay_title_bar()
while choice:
    # Get User Choice
    choice = get_choice()
    # Respond to User Choice
    dislay_title_bar()
    if choice == '1':
        show_games()
    elif choice == '2':
        get_new_game()
    elif choice == 'q':
        choice = ''
        quit()
    else:
        print('I did not quite get what you mean.')
        print('Can you repeat that?')
