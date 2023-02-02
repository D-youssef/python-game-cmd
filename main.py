import random

name = input("Enter your name : ")
user_score = 0
pc_score = 0
nuls = 0

while True :
    print(name,": ",user_score," Equal :",nuls,"Pc :",pc_score)
    user_shot = input("Input : (R)Rock,(C)Cisar,(P)Paper,(Q)QUITTER : ") # Rock => p  Cisar => c Paper => f

# function lower() to convert input to lower case
    shot = user_shot.lower()

# Q is to cancel the game
    if shot == "q" :
        print(" You Canceled the Game !")
        break
# if user input nothing we break the condition
    if shot != "f" and shot != "p" and shot != "c" :
        continue

    if shot == "p":
        print("Rock Vs ...",end=" ")
    elif shot == "f":
        print("Paper Vs ...",end=" ")
    else:
        print("Cisar Vs ...",end=" ")
# this number is special to laptop chosen by (pc)
    random_nbr = random.randint(1,3)
    if random_nbr == 1 :
        pc_shot = "p"
        print("Rock")
    elif random_nbr == 2 :
        pc_shot = "f"
        print("Paper")
    else :
        pc_shot = "c"
        print("Cisar")
# conditions special to user and pc i started with nulle
    if pc_shot == shot :
        print("Nul Game !")
        nuls = nuls + 1
    elif shot == "p" and pc_shot == "c" :
        print("You Win !")
        user_score = user_score + 1
    elif shot == "f" and pc_shot == "p" :
        print("You Win !")
        user_score = user_score + 1
    elif shot == "c" and pc_shot == "f" :
        print("You Win !")
        user_score = user_score + 1
    elif shot == "p" and pc_shot == "f" :
        print("You Loose !")
        pc_score = pc_score + 1
    elif shot == "f" and pc_shot == "c" :
        print("You Loose !")
        pc_score = pc_score + 1
    elif shot == "c" and pc_shot == "p" :
        print("You Loose !")
        pc_score = pc_score + 1
