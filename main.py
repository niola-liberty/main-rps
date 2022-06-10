import random
while True:
    opt = ['r', 'p', 's']
    player = input("Enter your choice; 'r' for rock, 'p' for paper and 's' for scissors:\n ")
    cpu = random.choice(opt)
    while player != 'r' and player != 'p' and player != 's':
        print("You chose "+ player)
        player = input("Enter valid option:\n")
    if player == 'r':
        if cpu == 's':
            print("Player: "+'r' +" CPU: " + 's')
            print("Rock beats scissors. You win!")
        else:
            print("Player: "+'r' +" CPU: " + 'p')    
            print("Paper beats rock. CPU wins :(")
    elif player == 'p':
        if cpu == 'r':
            print("Player: "+'p' +" CPU: " + 'r')
            print("Paper beats rock. You win!")
        else:
            print("Player: "+'p' +" CPU: " + 's')    
            print("Scissors beats paper. CPU wins :(")
    elif player == 's':
        if cpu == 'p':
            print("Player: "+'s' +" CPU: " + 'p')
            print("Scissors beats paper. You win!")
        else:
            print("Player: "+'s' +" CPU: " + 'r')    
            print("Rock beats scissors. CPU wins :(")
            break
    if player == cpu:
        print("Player: "+player +" CPU: " + cpu  )
        print("It's a tie!") 


  

            