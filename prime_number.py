# Write a prpgram to find whether the entered number is prime or not?

num = int(input("Enter a number: ")) # asking user to enter an number

if num > 1:
    for i in range(2, num):
        if (num % i) == 0:
            print(num, "is not a prime number")
            print(i, "times", num // i, "is", num)
            break
    else:
        print(num, "is a prime number")

else:               # if the user enters Zero or any Negative number when asked to enter initially
    print(num, "is not a prime number")
