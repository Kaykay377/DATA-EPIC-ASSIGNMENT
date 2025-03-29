-- Task 1: Check Even or Odd Numbers (1 to 15)
for num in range(1, 16):  
    if num % 2 == 0:
        print(f"{num} is even")
    else:
        print(f"{num} is odd")


--- Task 2: Simple Calculator
def calculator():
    try:
        # Get user input for two numbers
        num1 = float(input("Enter the first number: "))
        num2 = float(input("Enter the second number: "))
        
        # Get user choice for operation
        operation = input("Choose an operation (+, -, *, /): ")
        
        # Perform calculation
        if operation == "+":
            result = num1 + num2
        elif operation == "-":
            result = num1 - num2
        elif operation == "*":
            result = num1 * num2
        elif operation == "/":
            if num2 == 0:
                print("Error: Division by zero is not allowed.")
                return
            result = num1 / num2
        else:
            print("Invalid operation. Please choose +, -, *, or /.")
            return
        
        # Display result
        print(f"The result is: {result}")

    except ValueError:
        print("Invalid input! Please enter numeric values.")

# Run the calculator
calculator()
