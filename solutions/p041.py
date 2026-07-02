# Write a python program to onvert string to int without using library functions

# Step 1: Define a function to convert a string into an integer
def str_to_int (str):

    # Initialize the number, index, and sign
    num, i, sign = 0, 0, 1

    # Check if the number is negative
    if str[0] == '-':
        sign, i = -1, 1

    # Convert each character into its corresponding digit
    while i < len(str):
        num = num * 10 + int(str[i])
        i += 1
    
    # Return the integer with the correct sign
    return sign * num

# Step 2: Get the number in string format from the user
str = input("enter a number in string: ")

# Step 3: Call the function
res = str_to_int(str)

# Step 4: Get the result
print("the string in number is: ", res)