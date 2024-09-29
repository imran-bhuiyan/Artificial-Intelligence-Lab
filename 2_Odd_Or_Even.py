num=int(input("Enter a number: "))
divider=int(input("Enter divider: "))
if num%4==0:
    print("Divisible by 4")
elif num%2==0:
    print("Even")
else:
    print("Odd")
if num%divider==0:
    print(num," is evenly divided by ", divider)
else:
    print(num," is not evenly divided by ", divider)