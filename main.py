from replit import clear
from art import logo
bids = {}

#this part is redundant
# def add_Bidders(name_bidder, value_bidded):
#   bids[name_bidder] = value_bidded

def find_highest_bidder(bidding_record):
  highestValue = 0
  winner = ""
  for person in bidding_record:
    if bidding_record[person] > highestValue:
      highestValue = bidding_record[person]
      winner = person
  print(f"The winner is {winner}, who bid ${highestValue}.")

repeat = True
while repeat:
  print(logo)
  name = input("Welcome to the action, please tell your name: ")
  value = int(input("Please tell the value of your bid: "))
  # add_Bidders(name, value)
  bids[name] = value
  anotherPerson = input("Is there any other person to bide? answer with 'yes' or 'no': ").lower()
  if anotherPerson == 'no':
    repeat = False
  clear()
find_highest_bidder(bids)
