#Dustin Hasselbusch
#3/29/2026
#Module 1.3

def bottle(count: int) -> str:
    if count > 0: # instance for inevitible 0
        next_count = count - 1 #counts down
        current_bottle = "bottle" if count == 1 else "bottles" #user inputted number keeping track
        next_bottle: str = "bottle" if next_count == 1 else "bottles" #instance for 1, changed retroactively within program
        next_text = "no more" if next_count == 0 else str(next_count) #instead of 0 bottle(s), it will say "no more"
        song = (
            f"{count} {current_bottle} of beer on the wall, {count} {current_bottle} of beer.\n" 
            f"Take one down and pass it around, {next_text} {next_bottle} of beer on the wall.\n" + " \n"
        )
        return song + bottle(next_count) #calls the function again until 0 bottles then returns line 10

    return "No more bottles of beer on the wall, no more bottles of beer.\n" + " \n" + "Time to go to the store and get some more!\n"
    #when 0 bottles:

def Inputs() -> int: #returns int
    while True:
        amount = input("How many bottle(s)? (1-99): ")
        try:
            number = int(amount) #inputted number
            if number < 1 or number > 99:
                print("Please enter a whole number between 1 and 99.")
                continue
        except (ValueError, TypeError): #if inputted something else besides 1-99: give printed error and rerun line 17
            print("Invalid input. Please enter a whole number between 1 and 99.") 
            continue
        return number #if 1-99 is inputted:

if __name__ == "__main__": 
    count = Inputs() #allow user to input numbers of bottles
    print(bottle(count)) #runs song after correct input, 1-99
