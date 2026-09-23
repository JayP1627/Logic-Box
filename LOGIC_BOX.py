print("Welcome to the Pattern Generator and Number analyzer App.\n")

#here we use While loop , because we don't know how many time we have to iterate the loop.

while True:

    #here i make a variable "option" which store the value of option chosen by user.

    option=int(input("""Select an Option:                      
1. Pattern generator.
2. Number Analyzer.
3. Exit.\n 
Enter Your Choise: """))
    print()

    #it is the match-case for selecting  one option out of 3.

    match option:
        case 1:
            print("--------Now you are in Pattern Generator.--------")
            print("->It print the pattern of * of Right Angle Triangle.\n")

            rows=int(input("Enter Number Of Rows:"))

            print("Pattern:")

            for i in range(rows+1):
                for j in range(i):
                    print("*",end=" ")
                print()
            print("Your Pattern is generated.")
            print("Thank you For Using Pattern Generator.\n")

        case 2:
            print("--------Now you are in Number Analyzer.--------")
            print("->It simply take range from you and give Even and Odd numbers and also give sum of all number.\n")

            start=int(input("Enter starting range: "))
            stop=int(input("Enter stoping range: "))
            sum=0

            for i in range(start,stop+1):
                if i%2==0:
                    print(f"Number {i} is :Even")
                else:
                    print(f"Number {i} is :Odd")

                sum+=i
            print(f"\nSum of All numbers from {start} to {stop}= {sum}.\n")

        case 3:
            print("You are Exited.!")
            print("----------Thank you for using Logic Box App.----------")
            break
            # i used break statement here , because after choosing option 3 we have to exit from while loop.
        case _:
            print("Please Enter Your Choise between 1 to 3.\n")

            #here i make an else Match case for the user who exidently enter wrong value.
            