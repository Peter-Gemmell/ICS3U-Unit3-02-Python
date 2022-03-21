#!/usr/bin/env python3

# Created by Peter Gemmell
# Created on March 2022
# This program is a simple guessing game

import constants


def main():
    # this function makes a simple guessing game

    # input
    guess_Number = int(input("Guess a number between 0-9 : "))

    # process & output
    if guess_Number == constants.mystery_Number:
        print("You guessed correctly!")
    if guess_Number != constants.mystery_Number:
        print("You guessed incorrectly.")
    print("\nDone.")


if __name__ == "__main__":
    main()
