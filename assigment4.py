age = int (input("enter your age: "))
if age < 13:
    print("you are child.")
elif age >= 13 and age <= 19:
    print("you are teenager.")
elif age >= 20 and age <= 59:
    print("you are adult.") 
elif age >= 60:
    print("you are senior citizen.")
else: 
    print("invalid age.")


num = float(input("enter a number: "))

if num > 0:
    print ("the number is positive.")
elif num < 0:
    print ("the number is negative.")
else: 
    print("the number is zero.")

numbers = [10,20,30,40, 50]
print ("all number in the list:")

for num in numbers:
    print(num)

    print("last item in the list:")
    print(numbers[-1])
    

    
    mydata ={     
"name":"ali",
"age":21,
"city":"Karachi",


  } 
    
    mydata["country"] = "pakistan"

print(mydata)