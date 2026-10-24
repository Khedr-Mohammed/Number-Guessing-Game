# number-guessing-game.py
import random 

#Iinitialization Function and play function
def play_game () :
    high = 0
    low = 0
    win = 0

    #the random number 
    ran_number = random.randint(1,100) 

    #Gussing_condition 
    try :
        #condition
        while win == 0 :
            #input number
            my_number = int (input("Enter number for find the random number between 1 and 100 \n"))

            if my_number > ran_number :
                message = "your number is very high"
                high +=1 

            elif my_number < ran_number :
                message = "your number is very low"
                low +=1 

            else :
                message = "your number is the random number __mabrook"
                win +=1 

            print ()
            print (message)
    except ValueError:
        print ("\nInvailed_value ... please enter a number \n")

    #display all the counters 
    print ("counts of high_tries is :",high)
    print ("counts of low_tries is :",low)
    print ("counts of win_tries_guesses is :" , win + high + low )

    def main () :
        while True :
            play_game() 
            choice = input("Do you want to play again ? (yes or no)? \n") .lower() 
            if choice== "no" :
                print ("thanks for playing \n")
                break

    main ()