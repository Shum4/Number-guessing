import random
print("Number Guessing Game")

#using randint function to generate random number between 1-9
number=random.randint(1,60)
chances=0
print("Guess a number (between 1 and 60): ")

while chances<10:
    guess=int(input("Enter your guess: "))

    if guess==number:
        print("congrats you won!")
        break

    elif guess<number:
        print("your guess was too low: guess a number higher than",guess)

    else: 
        print("your guess was too high: guess a number lower than",guess)

    chances=chances+1

if not chances<10:
    print("you lose! the number was",number)
