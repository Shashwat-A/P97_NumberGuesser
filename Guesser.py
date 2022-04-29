import random

chances = 0
number = random.randint(0,10)
gNumber = round(number)
print("Number Guessing Game")
print(" ")
print("You have to guess the number from 0 to 10. You have 5 chances")

while chances < 5 :
    guess = int(input("Enter your guess - "))


    if(guess < gNumber) :
        print(" ")
        print("Your guess was low, guess higher than", guess)
    
    elif(guess > gNumber) :
        print(" ")
        print("Your guess was high, guess less than", guess)
    elif(guess == gNumber) :
        print(" ")
        print("Wow! You guessed it, correct answer was", guess)
        break
    
    chances = chances + 1

if(chances == 5) :
    print(" ")
    print("You Loose! The correct answer was", gNumber)