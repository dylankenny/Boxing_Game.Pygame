# Name: Dylan Kenny
# Student Number: 121352326

import random

#Using Fighter as a parent class

class Fighting:


     #Default constructor using only self as patameter
     #Child classes will inherit the parameters

     def __init__(self,name,health,jab,left_hook,right_hook,right_uppercut,left_uppercut):
          self.name = name
          self.health2 = 100
          self.health = health
          
          #punch selection
          self.jab = jab
          self.left_hook = left_hook
          self.right_hook = right_hook
          self.left_uppercut = left_uppercut
          self.right_uppercut = right_uppercut
          
     #Creating a function for choosing the punch you want to throw
     def Attack_selection(self,player2): 

          #Asking players what punch they want to throw
          print(self.name, "select what punch you want to throw ")
          punch_selection = int(input("1.) Jab \n2.) Left Hook \n3.) Right Hook\n4.) Left Uppercut\n5.) Right Uppercut \nSelect the punch you want to throw : "))
          print("-"*50)
          my_commentary = ["He is on the ropes","That was a good punch", "He is looking shakey","His knees just wobbled", "That was a good shot", "He's looking down and out"]   


          #Nested function
          #Gives Actions function access to Attack_selection variables and names

          def Actions(punch):
               #select a random block number form 0-5
               self.block = random.randint(0,5) 
               damage = punch - self.block
               #health of player decreses with damage absorbed
               player2.health2 = player2.health2 - damage
               
               #commentry for every punch
               print(self.name, "threw a", punch, "damage punch")
               print(player2.name, "blocked for", self.block, "health")
               print(self.name, "threw", damage, "damage to", player2.name)

               #when the health is less then 0, print health = 0
               if player2.health2 < 0 :
                    player2.health2 = 0
                    print(player2.name, "has", player2.health2, "health remaining")
               else:
                    print(player2.name, "has", player2.health2, "health remaining")
               print("-"*50)

               #random commentry after every punch
               print(random.choice(my_commentary))
               
               #Runs if Players are not knokced out
               if player2.health2 > 0:
                    return player2.Attack_selection(self)
               #else, the game is over
               else:
                    print(player2.name, 'HAS BEEN KNOCKED OUT!!!!!!!!!!!')

          #Calling Actions function above for punch selection
          if punch_selection == 1:
               #calling funtion with punch we want to throw
               Actions(self.jab)
          elif punch_selection == 2:
               #calling funtion with punch we want to throw
               Actions(self.left_hook)
          elif punch_selection == 3:
               #calling funtion with punch we want to throw
               Actions(self.right_hook)
          elif punch_selection == 4:
               #calling funtion with punch we want to throw
               Actions(self.left_uppercut)
          elif punch_selection == 5:
               #calling funtion with punch we want to throw
               Actions(self.right_uppercut)
          else:
               # if input is invalid ask them to try again
               x = (input("Invalid input , please select a number from 1-5 \nWant to try again(y/n): "))
               print(x)
               if x == "y":
                    # if answer is yes , they pick a number from 1-5 for the punch to throw
                    self.Attack_selection(player2)  
               else:
                    print("Thank you for playing ")


#Each one of my friends is a child class from the parent class Fighting

class Dylan(Fighting):
     def __init__(self):
          #inherits the arguments from Fighting class
          super().__init__("Dylan",100,5,12,12,16,16)
class Barra(Fighting):
     def __init__(self):
          #inherits the arguments from Fighting class
          super().__init__("Barra",100,5,6,6,12,12)              
class Eoin(Fighting):
     def __init__(self):
          #inherits the arguments from Fighting class
          super().__init__("Eoin",100,5,5,5,10,10)
class Mark(Fighting):
     def __init__(self):
          #inherits the arguments from Fighting class
          super().__init__("Mark",100,10,15,15,20,20)
class Rory(Fighting):
     def __init__(self):
          #inherits the arguments from Fighting class
          super().__init__("Rory",100,6,10,10,15,15)
class Sean(Fighting):
     def __init__(self):
          #inherits the arguments from Fighting class
          super().__init__("Sean",100,6,8,8,12,12)
class MarkB(Fighting):
     def __init__(self):
          #inherits the arguments from Fighting class
          super().__init__("MarkB",100,6,10,10,18,18)
class Darragh(Fighting):
     def __init__(self):
          #inherits the arguments from Fighting class
          super().__init__("Darragh",100,4,10,10,12,12)
        
class player1:

     def player_one(self):
          #Select your fighter
          player_class = input("Player 1, select your fighter: \n 1) Dylan \n 2) Mark \n 3) Barra \n 4) Eoin \n 5) Rory \n 6) Mark B \n 7) Sean \n 8) Darragh \n Player 1: ")
          if player_class == "1":
               # assigns player 1 to class depending on what value is entered
               player_class = Dylan()
               print("Player 1 has selected Dylan")
               #returns fighter selection
               return player_class
          elif player_class == "2":
               # assigns player 1 to class depending on what value is entered
               player_class = Mark()
               print("Player 1 has selected Mark")
               #returns fighter selection
               return player_class
          elif player_class == "3":
               # assigns player 1 to class depending on what value is entered
               player_class = Barra()
               print("Player 1 has selected Barra")
               #returns fighter selection
               return player_class
          elif player_class == "4":
               # assigns player 1 to class depending on what value is entered
               player_class = Eoin()
               print("Player 1 has selected Eoin")
               #returns fighter selection
               return player_class
          elif player_class == "5":
               # assigns player 1 to class depending on what value is entered
               player_class = Rory()
               print("Player 1 has selected Rory")
               #returns fighter selection
               return player_class
          elif player_class == "6":
               # assigns player 1 to class depending on what value is entered
               player_class = MarkB()
               print("Player 1 has selected Mark B")
               #returns fighter selection
               return player_class
          elif player_class == "7":
               # assigns player 1 to class depending on what value is entered
               player_class = Sean()
               print("Player 1 has selected Sean")
               #returns fighter selection
               return player_class
          elif player_class == "8":
               # assigns player 1 to class depending on what value is entered
               player_class = Darragh()
               print("Player 1 has selected Darragh")
               #returns fighter selection
               return player_class
          else:
               # if invalid please try again, calls player_one() function again for user to select a valid input
               print("Invalid input please select a number from 1-8")
               ans = self.player_one()
               return ans



class player2:

     def player_two(self):
          player_class = input("Player 2, select your fighter: \n 1) Dylan \n 2) Mark \n 3) Barra \n 4) Eoin \n 5) Rory \n 6) Mark B \n 7) Sean \n 8) Darragh \n Player 2: ")               
          if player_class == "1":
               # assigns player 2 to class depending on what value is entered
               player_class = Dylan()
               print("Player 2 has selected Dylan")
               #returns fighter selection
               return player_class
          elif player_class == "2":
               # assigns player 2 to class depending on what value is entered
               player_class = Mark()
               print("Player 2 has selected Mark")
               #returns fighter selection
               return player_class
          elif player_class == "3":
               # assigns player 2 to class depending on what value is entered
               player_class = Barra()
               print("Player 2 has selected Barra")
               #returns fighter selection
               return player_class
          elif player_class == "4":
               # assigns player 2 to class depending on what value is entered
               player_class = Eoin()
               print("Player 2 has selected Eoin")
               #returns fighter selection
               return player_class
          elif player_class == "5":
               # assigns player 2 to class depending on what value is entered
               player_class = Rory()
               print("Player 2 has selected Rory")
               #returns fighter selection
               return player_class
          elif player_class == "6":
               # assigns player 2 to class depending on what value is entered
               player_class = MarkB()
               print("Player 2 has selected Mark B")
               #returns fighter selection
               return player_class
          elif player_class == "7":
               # assigns player 2 to class depending on what value is entered
               player_class = Sean()
               print("Player 2 has selected Sean")
               #returns fighter selection
               return player_class
          elif player_class == "8":
               # assigns player 2 to class depending on what value is entered
               player_class = Darragh()
               print("Player 2 has selected Darragh")
               #returns fighter selection
               return player_class
          else:
               # if invalid please try again, calls player_two() function again for user to select a valid input
               print("Invalid input please select a number from 1-8")
               ans = self.player_two()
               return ans


# multiple inheritence so we can access the functions player_one() and player_two()
class play_game(player1,player2):
     
     #This is the intro to the game
     print("-"*50)
     print("WELCOME TO THE BROOKFIELD BOXING CHAMPIOSHIP")
     print("-"*50)
     print("WHO CAN OUTBOX WHO")
     print("-"*50)
     print("WE ARE GOING TO FIND OUT !!!!!")
     print("-"*50)
     
     def __init__(self):
          
          #use of pass avoids error message
          pass
                              
          #assigning functions to a variable  so we can call the functions
          p1 = self.player_one()
          p2 = self.player_two()
     

          #This is the intro to the fight when you select your fighters
          print("-"*50)
          print("LETS GET READY TO RUMBLE")
          print("-"*50)    
          print("Ref : I want a good clean fight between you two")
          print("-"*50)
          # class returned from player_one() and class returned from player_two() are ran in the funtion Attack_selection()
          p1.Attack_selection(p2) 

#run the game

play_game()
print("-"*50)
#If the players want to play again , they can choose new fighters
play_again = input("Would you like to play again(y/n): ") 
if play_again == "y":
     #run the game
     play_game()
else:
     #game
     print("Thank you for playing")
        
print("-"*50)






        

    
                

          

        


     
    

    


















