try:
    a = int(input("Enter the first number :"))
    b = int(input("Enter the second number :"))

    print("What kind of operation do you perform.\n1. Press + for addition\n2. Press - for subtraction\n3. Press * for multiplication\n4. press / for division")

    o = input("Enter operation :")
    # b = int(input("Enter the second number :"))


    match o:
        case "+":
            print(f"The result is {a+b}")
        
        case "-":
            print(f"The result is {a-b}")

        case "*":
            print(f"The result is {a*b}")

        case "/":
            print(f"The result is {a/b}")

        case default:
            print("There was an error")


except Exception as e:
    print("Enter a vlaue of a and b")


 

