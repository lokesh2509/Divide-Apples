n = int(input("Enter the number of apples you want to divide:- "))
mn = int(input("Enter the minimum range:- "))
mx = int(input("Enter the maximum range:- "))

for i in range(mn, mx+1):
    if mn == mx:
        print("This is not a range, and mn is equal to mx")

    if n%i == 0:
        print(f"{n} is divisible by {i}")

    else:
        print(f"{n} is not divisible by {i}")


