import random
print("Number Guessing Game")
number = random.randint(1, 9)
chances = 0
print("Guess The number Between 1 and 9")
while chances < 5:
    guess= int(input("enter your guess"))
    if guess == number :
        print("Congrants You Guess it Right Good Job great man!!!!!!!!!!!!!!!!!!!!!!!!")
    elif guess < number :
        print("Your Guess was too low, guess a higher number", guess)
    else : 
        print("Your Guess was Too High, Guess a lower Number", guess)
    chances = chances+1

if not chances < 5 : 
    print("You lose!!! The number is==>",number) 


