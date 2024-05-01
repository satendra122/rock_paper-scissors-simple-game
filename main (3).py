import random

print("Welcome to the Rock_Paper_scissors_Game\n")
rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

#Write your code below this line 👇
user_input = int(
    input(
        "What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n"
    ))
computer_choice = random.randint(0, 2)
if int(computer_choice == 0 and user_input == 0):
    print(
        f"Computer_choice:{computer_choice}\n{rock}\nYou choice:\n{rock}\n It's a draw"
    )
elif int(computer_choice == 0 and user_input == 1):
    print(
        f"Computer_choice:{computer_choice}\n{rock}\nYou choice:\n{paper}\n You Win"
    )
elif int(computer_choice == 0 and user_input == 2):
    print(
        f"Computer_choice:{computer_choice}\n{rock}\nYou choice:\n{scissors}\n You Win"
    )
elif int(computer_choice == 1 and user_input == 0):
    print(
        f"Computer_choice:{computer_choice}\n{paper}\nYou choice:\n{rock}\n You Lose"
    )
elif int(computer_choice == 1 and user_input == 1):
    print(
        f"Computer_choice:{computer_choice}\n{paper}\nYou choice:\n{paper}\n It's a draw"
    )
elif int(computer_choice == 1 and user_input == 2):
    print(
        f"Computer_choice:{computer_choice}\n{paper}\nYou choice:\n{scissors}\n You Won"
    )
elif int(computer_choice == 2 and user_input == 0):
    print(
        f"Computer_choice:{computer_choice}\n{scissors}\nYou choice:\n{rock}\n You Lose"
    )
elif int(computer_choice == 2 and user_input == 1):
    print(
        f"Computer_choice:{computer_choice}\n{scissors}\nYou choice:\n{paper}\n You Lose"
    )
elif int(computer_choice == 2 and user_input == 2):
    print(
        f"Computer_choice:{computer_choice}\n{scissors}\nYou choice:\n{scissors}\n It's a draw"
    )
else:
    print("Sorry you choose invalid number!")
