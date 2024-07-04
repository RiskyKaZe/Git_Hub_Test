print("This is my First Useful Piece of Code that I am going to Publish on GitHub!")

tot = 0.0

while True:

    num = str(input("Enter the Number to Add to the Running Total: "))

    try:

        num = float(num)
        tot = tot + num

    except ValueError:

        if num == "":
            print(f"The Running Total for the Numbers Entered is: {tot}")
        
        else:
            print("Your Input was not a Valid Number!")
            print(f"The Running Total for the Valid Numbers Entered Until Now is: {tot}")
        
        break

    