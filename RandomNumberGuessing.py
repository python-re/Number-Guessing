#---------------------------------------------------------------------------------------
# Import the RNG module.
import random
#---------------------------------------------------------------------------------------
# Beginning of file inclues: a welcome message and how many attemps you have
# to guess the number the RNG module is thinking of.

print("I'm feeling generous... Here's TEN attempts. Don't waste them now!")
print("Let's Begin! I'm thinking of a number between 1 and 50...\n")
#---------------------------------------------------------------------------------------
# Initiate the RNG, give it a range of 1 through 50 (1-50), and assigned it to
# the variable "randomInteger."
# randomInteger = random.randint(1,50) (moved to main method).
#---------------------------------------------------------------------------------------
# Assign a variable called "attempts" with an integer value of 0. This value
# will increment everytime it goes through the loop until the alloted attempts
# have been reached.
# attempts = 0 (moved to main method).
#---------------------------------------------------------------------------------------
# Main Function Code:

def main(randomInteger = random.randint(1,50), attempts = 0):

    # While you have enough attempts, allow the user to guess a number.
    while (attempts < 10):

        
        # Ask the user to input a guess.
        gatherUserInput = int(input("Enter a guess: "))


        # If the user's guess matches the RNG module's, print that you guess right.
        if (gatherUserInput == randomInteger):
            print("You guessed the integer RIGHT! The number was: " + str(randomInteger))
            break
        
                    # Break isn't neccessarily a good idea in the programs I work with, but
                    # for the sake of this one, I will use it to immediately stop the running
                    # module.


        # If the user's guess is greater than the RNG module's, print that it's too high.
        if(gatherUserInput > randomInteger):
            print("Your guess of: " + str(gatherUserInput) + " was too high.\n")


        # If the user's guess is less than the RNG module's, print that it's too low.
        if(gatherUserInput < randomInteger):
            print("Your guess of: " + str(gatherUserInput) + " was too low.\n")


        # Incrememnt the number of attempts. Everytime this happens you lose an attempt
        # so ten attempts becomes nine and so on...
        attempts += 1


        # Used all ten attempts? Then terminate the program.
        if (attempts == 10):
            print("You didn't guess my number which was: " + str(randomInteger))
            print("Program has been terminated :-(.")
            break

                    # Once again, break isn't neccessarily a good idea in the programs I work with,
                    # but for the sake of this one, I will use it to immediately stop the running
                    # module.
#---------------------------------------------------------------------------------------
# Finally, call the main method so that the entire program runs. This program
# is contained inside one giant main function (known as a method in Java IDE's)
main()
