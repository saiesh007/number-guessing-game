import random
randNumber = random.randint(1, 100)
userGuess = None                        # Otherwise will get not defined error
guesses = 0

while(userGuess != randNumber):
    userGuess = int(input("Enter your guess: "))
    guesses += 1
    if(userGuess==randNumber):
        print("You guessed it right!")
    elif(userGuess>randNumber):
        print("You guessed it wrong! Enter a smaller number")
    else:
        print("You guessed it wrong! Enter a larger number")

print(f"You guessed the number in {guesses} guesses")
with open("hell.txt", "r") as f:
    hiscore = int(f.read())

if(guesses<hiscore):
    print("You have just broken the high score!")
    with open("hell.txt", "w") as f:
        f.write(str(guesses))
