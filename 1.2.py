1.2 Develop a Python program for Recursion using factorial

AIM:
To Develop a Python program for Recursion using factorial

Algorithm:
Step 1: Start
Step 2: Get a Number from User(N)O
Step 3 : write a function for factorial
step 4 : fact = fact*fact(N-1)
step 5: display result
Step 6: Stop

Program:
#Develop a Python program for Recursion using factorial
n=int(input("Enter a Number:"))
print("Factorial:")
def fact(n):
  if n==0 or n==1:
    return 1

  else:
    return n * fact(n-1)
print(fact(n))

Result:
Thus the program has been executed successfully.
