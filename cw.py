def main():
    #problem1()
    #problem2()
    #problem3()
    problem4()

#Create a random number. Print the number.


#def problem1():
    #import random
    #randomNum= random.randint(0,200)
    #print(random.randint(0,200))


#Create a function that has a loop that quits with ‘q’.
# If the user doesn't enter 'q', ask them to input another string.

#def problem2():
    #while True:
        #letter=input("Enter a letter.")
       #if(letter=="q"):
            #break
        #else:
            #print("TRY AGAIN")

#Create a function that will loop until the user enters '0'.
# Ask the user to enter a positive integer number.
# Print 0 to that number and ask them again to enter a number until they enter '0'. Repeat.


def problem3():
    while True:
        maxnum=int(input("Enter a postive number."))
        if(maxnum ==0):
            break
        for num in range(0,(maxnum+1)):
            print(num)

#Create a function that creates a random number. Ask the user to guess the random number.
# Keep letting the user guess until they get it right, then quit.
# If they don't get it right, tell them if their next guess has to be higher or lower.


def problem4():
    import random
    myrand=int(input("Gues a random number."))
    randomnum= random.randint(0,5)
    while(myrand!=randomnum):
        myrand=int(input("Guess a random number"))













if __name__ == '__main__':
    main()