num1 = float(input("Enter the First value: "))
num2 = float(input("Enter the Second value: "))
num3 = float(input("Enter the Third value: "))
if (num1 < num2 and num1 < num3):
          print(num1," < ", num2 ," < " ,num3)
elif (num2 < num1 and num2 < num1):
          print(num2," < ", num1," < ",num3)
elif (num3 < num1 and num3 < num2):
          print(num3," < ",num1," < ",num2)
else:
          print("Either any two values or all the three values are equal")