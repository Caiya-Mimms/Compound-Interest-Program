# Caiya Mimms | Jan 28,2023
# Compound_Interest_Program | HW #2.14
# Calulates the balance of an account after a specified number of years (4 User Inputs)

#Welcome text 
print("Hi there! This program calulates the balance of an account after a specified number of years.")

    #INPUTS

    #Defining P,r,n,and t
P = float(input("What is the amount of principal originally deposited into the account: "))
r = float(input("What is annual interest rate paid by the account: "))
n = float(input("What is number of times per year that the interest is compounded? (Compounded monthly, enter 12. Compounded quarterly, enter 4.): "))
t = float(input("What is number of years the account will be left to earn interest?: "))

    #Apllying Formula

r /= 100
a = P * (( 1 + (r / n))**(n * t))

    #Rounding for simplicity
A =round(a * 100.00)/100.00

    #Printing calulation

print("The amount of money that will be in the account after",t,"years is",A,".")
print("End Program.")