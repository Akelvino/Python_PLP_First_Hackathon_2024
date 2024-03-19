age = int(input("Enter your age \n"))

if age<=0:
    print("Enter a valid age")
    
elif age<18:
    print("You are not eligible to vote")
else:
    print("you are eligible to vote")