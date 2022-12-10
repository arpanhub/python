from random import randint  #To generate a random number
name = input("Please Enter your name: ")
s=1
def game():
    print()
    print("Welcome to my Number game, " + name)
    print("enter the lower and upper bound range to start the game")
    l=int(input("lower bound= "))
    u=int(input("upper bound= "))
    rand_number = randint(l,u)   #Generates a random number
    print("\nI have selected a number between",l,"and",u)
    print("You have 3 chances to guess that number...")
    i = 1
    r = 1
    s = 0
    while i<4:  #3 Chances to the user
        user_number = int(input('Enter your number: ')) 
        if user_number < rand_number:
            print("\n" + name + ", My number is greater than your guessed number")
            print("you now have " + str(3-i)+ " chances left" )
            i = i+1
        elif user_number > rand_number:
            print("\n" + name + ", My number is less than your guessed number")
            print("you now have " + str(3-i)+ " chances left" )
            i = i+1
        elif user_number == rand_number:
            print("\nCongratulations "+name+"!! You have guessed the correct number!\n")
            s= s+1
            r = 0;
            break
        else:
            print("This is an invalid number. Please try again")
            print("you now have " + str(3-i)+ " chances left" )
            continue
    if r==1:
        print("Sorry you lost the game!!")
        print("My number was = " + str(rand_number))

def main():
    game()
    print("your score",s)
    while True:
        another_game = input("Do you wish to play again?(y/n): ")
        if another_game == "y":
            game()
            print("your score",s)
        else:
            break
main()
print("\nEnd of the Game! Thank you for playing!")
