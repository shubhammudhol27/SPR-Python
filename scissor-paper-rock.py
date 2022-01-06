import os

player1_name = input("Enter 1st Player Name: ")
player2_name = input("Enter 2nd player Name: ")

os.system('cls' if os.name == 'nt' else 'clear')

print("--------------------------------------------------------")
print(" ╔═╗┌─┐┬┌─┐┌─┐┌─┐┬─┐   ╔═╗┌─┐┌─┐┌─┐┬─┐   ╦═╗┌─┐┌─┐┬┌─┬")
print(" ╚═╗│  │└─┐└─┐│ │├┬┘   ╠═╝├─┤├─┘├┤ ├┬┘   ╠╦╝│ ││  ├┴┐│")
print(" ╚═╝└─┘┴└─┘└─┘└─┘┴└─┘  ╩  ┴ ┴┴  └─┘┴└─┘  ╩╚═└─┘└─┘┴ ┴o")
print("         ~ [ WELCOME TO S.P.R GAME BY HANSANA ] ~")
print("--------------------------------------------------------")   
print(" Please select a number below to use the options, ")
print("----------------------------------------------")
print(" ~ Rock --> 1 \n ~ Paper --> 2 \n ~ Scissor --> 3 ")
print("----------------------------------------------")

player1 = input("[" + player1_name + "]" + " Enter Your Choice: ")
os.system('cls' if os.name == 'nt' else 'clear')

print("--------------------------------------------------------")
print(" ╔═╗┌─┐┬┌─┐┌─┐┌─┐┬─┐   ╔═╗┌─┐┌─┐┌─┐┬─┐   ╦═╗┌─┐┌─┐┬┌─┬")
print(" ╚═╗│  │└─┐└─┐│ │├┬┘   ╠═╝├─┤├─┘├┤ ├┬┘   ╠╦╝│ ││  ├┴┐│")
print(" ╚═╝└─┘┴└─┘└─┘└─┘┴└─┘  ╩  ┴ ┴┴  └─┘┴└─┘  ╩╚═└─┘└─┘┴ ┴o")
print("         ~ [ WELCOME TO S.S.M GAME BY HANSANA ] ~")
print("--------------------------------------------------------")
print(" Please select a number below to use the options, ")
print("----------------------------------------------")
print(" ~ Rock --> 1 \n ~ Paper --> 2 \n ~ Scissor --> 3 ")
print("----------------------------------------------")

player2 = input("[" + player2_name + "]" + " Enter Your Choice: ")
os.system('cls' if os.name == 'nt' else 'clear')

print("======================================")

if player1 == "1" and player2 == "2":
    print(" " + player1_name + " Is the Winner! :)")

elif player1 == "1" and player2 == "3":
    print(" " + player1_name + " is the Winner! :)")

elif player1 == "2" and player2 == "1":
    print(" " + player1_name + " is the Winner! :)")

elif player1 == "2" and player2 == "3":
    print(" " + player2_name + "is the Winner! :)")

elif player1 == "3" and player2 == "1":
    print(" " + player1_name + " is the Winner! :)")

elif player1 == "3" and player2 == "2":
    print(" " + player1_name + " is the Winner! :)")

elif player1 == player2:
	print(" It's a tie. Play Again!")

else:
    print("Something Went Wrong. :(")
print("======================================")
print("   ________   __  _______  ____ _   _________  __")
print("  / ___/ _ | /  |/  / __/ / __ \ | / / __/ _ \/ /")
print(" / (_ / __ |/ /|_/ / _/  / /_/ / |/ / _// , _/_/ ")
print(" \___/_/ |_/_/  /_/___/  \____/|___/___/_/|_(_)")
print("")
print("~ Developed By @HansanaDasanayaka \n-------------------------------------- ")

