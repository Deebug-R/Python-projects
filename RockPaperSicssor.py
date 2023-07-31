import random 
while True:
    def person_check():
        per = input("You      :").lower()
        if per not in value:
            return person_check()
        return per
    value = ['rock','paper','scissors']
    computer = random.choice(value)
    print("Lets Start the Game:")
    print("Enter 'Rock' or 'paper' or 'Scissors':")
    person = person_check()

    print(f"Computer :{computer}")
    if person == computer:
        print(" tie....!")
    elif person == 'rock':
         if computer == 'paper':
            print("Computer win")
         else :
            print("You win")
    elif person == 'paper':
         if computer == 'scissors':
            print("Computer win")
         else :
            print("You win")
    elif person == 'scissors':
         if computer == 'rock':
            print("Computer win")
         else :
             print("You win")
    check = input("Continue to play press Enter or Exit press q ").lower()
    if check == 'q':
        break
    
