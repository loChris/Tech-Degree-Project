
import random
import os

high_score = 0
leaderboard = []
def start_game(high_score, leaderboard):
    print("=== WELCOME TO GUESS THAT NUMBER ===\n")
    print("Your high score is {}\n".format(high_score))
    print("Rules: This program will randomly select a number from 1 - 10. Try to guess the correct number.")
    print("We'll let you know if you're too high or too low! GLHF\n")
    print("Get Ready to start guessing. Input your number!")

    random_number = int(random.randint(1,10))
    attempt = 1

    while True:
        try:
            guess = int(input("> "))
        except ValueError:
            print("Invalid input.")
        else:
            if guess == random_number:
                print("Got it! {} was correct.".format(guess))
                print("It took you {} attempt(s) to succeed.\n".format(attempt))
                while True:
                    new_game = input("Would you like to start a new game? Yes/No  ")
                    if new_game.lower() == 'yes':
                        leaderboard.append(attempt)
                        high_score = min(leaderboard)
                        start_game(high_score, leaderboard)
                    elif new_game.lower() == 'no':
                        print("Thank you for playing!")
                        os._exit(0)
                    else:
                        print("Invalid input")
            elif guess < random_number:
                if guess < 1:
                    print("You're outside of the number range; Too low. Remember: 1 - 10!")
                    attempt += 1
                else:
                    print("Oops! Try Again. It's higher than {}.".format(guess))
                    attempt += 1
            elif guess > random_number:
                if guess > 10:
                    print("Try again. You're outside of the number range; Too high. Remember: 1 - 10")
                    attempt += 1
                else:
                    print("Oops! Try again. It's lower than {}.".format(guess))
                    attempt += 1
start_game(high_score, leaderboard)