import random

print("Welcome to the Guesser")
print("Choose your Fate!")

level = input("| For Easy - type 'E'| For Medium - type 'M' | For Hard - type 'H' |     ").upper()


def create_guess():
    # Random number and tries generation based on level
    if level == "E":
        correct_guess = random.randint(1, 10)
        tries = 6
        return correct_guess, tries
    elif level == "M":
        correct_guess = random.randint(1, 20)
        tries = 4
        return correct_guess, tries
    elif level == "H":
        correct_guess = random.randint(1, 50)
        tries = 3
        return correct_guess, tries


def check_guess():
    correct_guess, tries = create_guess()
    while tries > 0:
        # Accept user input
        user_guess = input("Guess a number   ")
        if user_guess == correct_guess:
            print("You got it right , awesome! ")
            break
        elif user_guess != correct_guess:
            # Reduce the number of tries
            tries = tries - 1
            if tries != 0:
                # Add plural statement if plural or not
                if tries > 1:
                    plural = "es"
                else:
                    plural = " "
                # Print number of remaining tries
                print("That was wrong. You have {} guess{} left".format(tries,plural))
            else:
                print("GAME OVER!")
                # Restart or end game as user pleases
                play_again = input("Would you like to Play again? (Y)es or (N)o     ")
                if play_again == "Y":
                    create_guess()
                    check_guess()


create_guess()
check_guess()
