#importing modules
import random
import time

def intro():
    print('''
██████╗░███████╗████████╗  ██╗████████╗  ░█████╗░███╗░░██╗██████╗░  ░██████╗░███████╗████████╗
██╔══██╗██╔════╝╚══██╔══╝  ██║╚══██╔══╝  ██╔══██╗████╗░██║██╔══██╗  ██╔════╝░██╔════╝╚══██╔══╝
██████╦╝█████╗░░░░░██║░░░  ██║░░░██║░░░  ███████║██╔██╗██║██║░░██║  ██║░░██╗░█████╗░░░░░██║░░░
██╔══██╗██╔══╝░░░░░██║░░░  ██║░░░██║░░░  ██╔══██║██║╚████║██║░░██║  ██║░░╚██╗██╔══╝░░░░░██║░░░
██████╦╝███████╗░░░██║░░░  ██║░░░██║░░░  ██║░░██║██║░╚███║██████╔╝  ╚██████╔╝███████╗░░░██║░░░
╚═════╝░╚══════╝░░░╚═╝░░░  ╚═╝░░░╚═╝░░░  ╚═╝░░╚═╝╚═╝░░╚══╝╚═════╝░  ░╚═════╝░╚══════╝░░░╚═╝░░░

██╗████████╗
██║╚══██╔══╝
██║░░░██║░░░
██║░░░██║░░░
██║░░░██║░░░
╚═╝░░░╚═╝░░░\n\n\n\n''')
    

    print("𝕸𝖆𝖉𝖊 𝖇𝖞 𝕿𝖆𝖓𝖒𝖆𝖞 𝕭𝖍𝖆𝖗𝖉𝖜𝖆𝖏\n\n\n")
def space():
    print("\n\n")

intro()
#Aquiring User data
user=input("enter your name here: ")

space()
age=int(input("enter your age here: "))

space()

#Age test
if age<12:
    print("You are underage to play this game")
    exit()
else: 
    pass

global principal_amount
principal_amount=10000

def rules():
    
    print("RULES")
    time.sleep(1)
    print(f"1. {user} you will have {principal_amount} as your starting amount.\n")
    print(f"2. You will get a dice consisting of the highest number 9.\n")
    print(f"3. You can bet maximum the amount you have. The betted amount will be subtracted from your principle amount at time of betting.\n")
    print(f"4. If you get an odd number when the dice is rolled then your betted amount will double.\n")
    print(f"5. and if you get an even number when the dice is rolled then your betted money will become zero\n")
    print(f"6. You can play unless you run out of money or decide to exit the game.\n")
    user_conformation= input("are you sure you want to continue? (yes/no)")
    if user_conformation=="yes":
        print("All the best!!!\n")
    else:
        exit()

    print("Loading game ........")

space()

def game_logic():

    while principal_amount!=0:
        player_choice=input("Do you agree to all the rules? (yes/no) ")
        space()
        while player_choice!="no":
            print(f"You have {principal_amount} amount.")
            betted_amount=int(input("Enter the amount you want to bet: "))
            space()
            def bet_check():

                if betted_amount<=principal_amount:
                    pass
                else:
                    print(f"Your betted amount is greater than {principal_amount}")
                    exit()

            bet_check()
            time.sleep(1)
            input("Press enter to roll the dice: ")

            def dice_roll():
                global principal_amount
                principal_amount=principal_amount
                global remaining_amount
                remaining_amount=principal_amount-betted_amount

                dice_roll_value=random.randrange(1,10)

                if dice_roll_value%2==0:
                    print(f"Yay you got {dice_roll_value}")
                    time.sleep(1)
                    print(f"Your profit is {betted_amount*2}")
                    space()
                    principal_amount=principal_amount-betted_amount+(betted_amount*2)
                    time.sleep(1)
                    print(f"Your total money is {principal_amount}")
                    space()
                    user_choice=input("Do you want to play further? (yes/no)")
                    space()
                    if user_choice=="no":
                        print("Thank you for playing with us. Se you again")
                        exit()
                    else:
                        pass
                elif principal_amount==0:
                    print("Thank you for playing better luck next time.")
                    exit()
                else:
                    print(f"Oh no ! better luck next time you got {dice_roll_value}")
                    space()
                    time.sleep(1)
                    print(f"Your betted money is 0 now.")
                    space()
                    principal_amount=principal_amount-betted_amount
                    time.sleep(1)
                    print(f"Your total money is {principal_amount}")
                    if principal_amount==0:
                        print("Oh no! you ran out of money.")
                        exit()
                    else:
                        pass

                    user_choice=input("Do you want to play further? (yes/no)")
                    space()
                    if user_choice=="no":
                        print("Thank you for playing with us. Se you again")
                    else:
                        pass
                    
            dice_roll()
        else:
            exit()

    else:
        exit()


rules()
game_logic()