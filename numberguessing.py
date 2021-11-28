import random

print('Number Guessing Game')
print('Guess a number between 1 and 9')

b = random.randint(1,9)

chances = 0

while chances<5:
    a = int(input("Enter your guess: "))

    if (a == b):
        print("Congratulations! You win.")
    
    elif (a < b):
        print("Your Guess is too Low")
        print("Guess a number higher than this")

    else:
        print("Your Guess is too high")
        print("Guess a number lower than this")
    
    chances+=1

if chances==5 and a!= a:
    print("YOU LOSE, the number is ", a)