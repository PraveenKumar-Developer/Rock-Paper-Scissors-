import random

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
game=[rock,paper,scissors]
user=int(input("what you choose ? type 0 for rock ,type 1 for paper or 2 for scissors : "))
if(user<3):
 print(game[user])
computer=random.randint(0,2)
print(f"comput choice {computer}")
print(game[computer])
if user==0 and computer==1:
  print("You Lose !!")
elif user==0 and computer==2:
  print("You Win !!")
elif user==1 and computer==2:
  print("You Lose !!")    
elif user==1 and computer==0:
  print("You Win !!")
elif user==2 and computer==1:
  print("You Win !!")
elif user==2 and computer==0:
  print("You Lose !!")
elif user==computer:
  print("match is draw")
else:
  print("You Entered a invalide number")