import time
import random
print("Welcome! Let's play a guessing game!")

time.sleep(1)
print("Try your luck!")

time.sleep(1)
print("For the game, you need to select a range of numbers within which you'd like to guess the number")

time.sleep(1)
lowerBound = int(input("Please enter the minimum value of your range: "))
upperBound = int(input("Please enter the maximum value of your range: "))

numberOfTries = 0

guessedNumber = random.randrange(lowerBound, upperBound + 1)
print(guessedNumber)

lastLowerBound = lowerBound
lastUpperBound = upperBound

playerNumber = int(input("It's your turn to guess a number! Enter your guessed number: "))

while True:
    if playerNumber > upperBound or playerNumber < lowerBound:
        playerNumber = int(input("You guessed a number beyond your specified range! Try Again something beyond your mentioned range!: "))

    else: 
        if playerNumber != guessedNumber and playerNumber > guessedNumber:
            print(f"Now you need to guess between {lastLowerBound} and {lastUpperBound}")
            playerNumber = int(input("Try Again! You guessed too high!: "))
            numberOfTries += 1
        
        
        elif playerNumber != guessedNumber and playerNumber < guessedNumber:
            print(f"Now you need to guess between {lastLowerBound} and {lastUpperBound}")
            playerNumber = int(input("Try Again! You guessed too low!: "))
            numberOfTries += 1
        
            
        else:
            break
            print(f"You win! You guessed the correct number in {numberOfTries} tries!")