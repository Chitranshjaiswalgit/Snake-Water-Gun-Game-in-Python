# Snake water Gun Game in Python
import random


def game(comp, user):
    if comp == user:
        return 0

    if comp == 0 and user == 1:
        return -1

    if comp == 1 and user == 2:
        return -1

    if comp == 2 and user == 0:
        return -1

    return 1


print("\n\n***** Welcome to the SNAKE WATER GUN GAME *****\n")
comp = random.randint(0, 2)
print("\n0 : Snake, 1 : water and 2 : Gun\n")
user = int(input("Enter your choice : "))

score = game(comp, user)

print("You : ", user)
print("Computer : ", comp)

if score == 0:
    print("\nIts a draw")
elif score == -1:
    print("\nYou Lost")
else:
    print("\nCongrats, You Won")

print("\nGAME OVER")
print("\n\n*** Thanks for Playing SNAKE WATER GUN GAME ***\n")
