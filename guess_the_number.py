import random


Rand_num=random.randint(1,100)


while True:
    guess=input("Guess an integer between 1 and 100 or Quit(Q):")

    if(guess=='Q'):
        print("!!!!YOU QUIT GAME!!!!")
        break

    guess=int(guess)
    if(guess==Rand_num):
        print("YOU GUESSED THE CORRECT NUMBER :)")
        break

    elif(guess<Rand_num):
        print("TRY A GREATER NUMBER")

    else:
        print("TRY A SMALLER NUMBER") 


print("----------GAME OVER---------")