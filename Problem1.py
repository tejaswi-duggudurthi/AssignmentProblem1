input1 = int(input("Enter the value1:"))
input2 = int(input("Enter the value2:"))
input3 = int(input("Enter the value3:"))
input4 = int(input("Enter the value4:"))
input5 = int(input("Enter the value5:"))

x = open("totalSum.txt","a")
totalSum = input1+input2+input3+input4+input5

print("totalSum:",totalSum,file=x)
print("totalSum:",totalSum)