print("Calculator")


fno = int(input("Give the first number: "))
sno = int(input("Give the second number: "))

while True:
    print("(1) +")
    print("(2) -")
    print("(3) *")
    print("(4) /")
    print("(5)Change numbers")
    print("(6)Quit")
    
    print("Current numbers:", fno, sno)
    smth = input("Please select something (1-6): ")
    
    if smth == "1":
	    print("The result is:", fno+sno)
    if smth == "2":
	    print("The result is:", fno-sno)
    if smth == "3":
	    print("The result is:", fno*sno)
    if smth == "4":
	    print("The result is:", fno/sno)
    if smth == "5":
        fno = int(input("Give the first number: "))
        sno = int(input("Give the second number: "))
    if smth == "6":
        print("Thank you!")
        break
