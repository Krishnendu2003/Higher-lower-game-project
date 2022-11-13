from art import logo,vs
import random
from game_data import data
from replit import clear
#format the game data for printable format
def format_data(account):
  """Format account into printable format: name, description and country"""
  account_name=account["name"]
  account_descr=account["description"]
  account_country=account["country"]
  return(f"{account_name},a {account_descr},from{account_country}")

#check if user is correct
def check_answer(guess,a_followers,b_followers):
  """Checks followers against user's guess 
  and returns True if they got it right.
  Or False if they got it wrong."""
  if a_followers > b_followers:
    return guess=="a"
  else:
    return guess=="b"


def game():

  account_a=random.choice(data)
  account_b=random.choice(data)
  game_should_continue=True
  while(game_should_continue): 
  
    
    print(logo)
    account_a=account_b
    account_b=random.choice(data)
    
    
    #Generate a random account from the game data
    
    if account_a == account_b:
      account_b=random.choice(data)
    
    a_follower_count=account_a["follower_count"]
    b_follower_count=account_b["follower_count"]
    #ask user for a guess
    print(f"Compare A :{format_data(account_a)} ")
    print(vs)
    print(f"Against B :{format_data(account_b)}  ")
    
    guess=input("Who has more followers? Type 'A' or 'B': ").lower()
  
    is_correct=check_answer(guess,a_follower_count,b_follower_count)
    score=0
    clear()
    print(logo)
    #Give user a feedback & #score keeping
    if is_correct:
      score+=1
      print(f"You are right , current score {score}")
      
    else:
      print(f"Sorry you are wrong , Final score {score}")
      game_should_continue=False
      
    
    
    
game()    
   
    
    
    
    
  
  
  
  
   
  
  

   















#making account at position b to position a






# clear screen