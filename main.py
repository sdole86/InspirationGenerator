import random


# sayings must be a list of sayings
sayings = [
        'Today will be a wonderful day!',
        'You are going to realize your dreams!',
        'Soon your ideas will be appreciated by others!',
        'Doors are opening because of your hard work!',
        'Your dreams are about to come true.']



count_sayings = len(sayings)


def get_saying():
    user_playing = True

    # enter into a loop while the user wants to continue to play
    while user_playing:
        # random_quote = sayings[random.randint(0, count_sayings)]  # get a random index value
        random_quote = random.choice(sayings)  # get a random index value
        print('\n')
        print('----- Your Saying for Today -----')
        print(random_quote)  # print the random saying

        print('\n')

        user_response = input("Would you like another inspirational saying? y/n:")
        if user_response.lower() != ("y"):
            user_playing = False


get_saying()
# print final message as the game play ends.
print('Thank you for playing, please come again.')
