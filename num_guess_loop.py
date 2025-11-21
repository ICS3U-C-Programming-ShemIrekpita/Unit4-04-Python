#!/usr/bin/env python3
# Created by: Shem
# Created on: 11/21/2025
# This program generates a random number and asks the user to guess it.
# It uses a loop and handles invalid input safely.

import random

def main():
    # Generate a random number between 1 and 10
    correct_number = random.randint(1, 10)
    while True:
        try:
            # Ask user to guess the number
            guess = int(input("Enter your guess (1 - 10): "))
            if guess == correct_number:
                print("You guessed it! The number was", correct_number)
                print("Thank you for playing")
                print(" /\\_/\\  ")
                print("( ^_^ )")
                print(" > ^ < ")
                break  # Exit the loop
            else:
                print("Wrong guess, try again!")
        except ValueError:
            # Handles invalid entries 
            print("Invalid entry! Please enter a whole number.")

if __name__ == "__main__":
    main()
