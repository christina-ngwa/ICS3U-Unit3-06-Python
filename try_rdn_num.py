#!/usr/bin/env python3

# Created by: Christina Ngwa
# Created on: October 2019
# this program checks if the user guess the number
#    with a try statement


import random


def main():
    # this function uses a try statement

    # input
    print("Guess what number I'm thinking of! (between 1 & 100)")
    randomanswer = random.randint(1, 100)  # a number between 1 and 100
    guess = input("Enter your guess: ")
    print("")

    # process
    try:
        guess_as_num = int(guess)
        if guess_as_num == randomanswer:
            # output
            print("You are correct!")
        else:
            print("Sorry, the number I was thinking of was", randomanswer, ".")
    except Exception:
        print("Wrong input. Try again.")
    finally:
        print("Thanks for playing.")


if __name__ == "__main__":
    main()
