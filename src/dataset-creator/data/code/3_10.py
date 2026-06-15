def calculate_division(num1, num2):
    try:
        result = num1 / num2
        print(f"The result of dividing {num1} by {num2} is: {result}")
    except ZeroDivisionError:
        print("Error: Cannot divide by zero.")
    except TypeError:
        print("Error: One or both inputs were not valid numbers.")
if __name__ == '__main__':
    num1 = 10
    num2 = 2
    calculate_division(num1, num2)