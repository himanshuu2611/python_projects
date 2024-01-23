import random

def game(comp,you):
    if comp=='s':
        if you=='w':
            print("Loose")
        elif you=='g':
            print("Win")
    elif comp=='w':
        if you=='s':
            print("win")
        elif you=='g':
            print("loose")
    elif comp==you:
        print("Tie !")
    elif comp=='g':
        if you=='s':
            print("Loose")
        elif you=='w':
            print("Win")

print("Computer  Turn : Snake(s) Water(w) or Gun(g) ? ")
rand=random.randint(1,3)
print(rand)
if rand==1:
    comp='s'
    print('s')
elif rand==2:
    comp='w'
    print('w')
elif rand==3:
    comp='g'
    print('g')

You=input("Your's Turn : Snake(s) Water(w) or Gun(g) ? ")

print(game(comp,You))
