def divide_numbers(a, b):
    try:
        result = a / b
        return result
    except ZeroDivisionError:
        return "Error: Cannot divide by zero."
    except TypeError:
        return "Error: Invalid input types. Please enter numbers."
if __name__ == '__main__':
    num1 = 10
    num2 = 2
    result = divide_numbers(num1, num2)
    print(f"The result of dividing {num1} by {num2} is: {result}")
    num1 = 10
    num2 = 0
    result = divide_numbers(num1, num2)
    print(f"The result of dividing {num1} by {num2} is: {result}")
    num1 = 5.5
    num2 = 2
    result = divide_numbers(num1, num2)
    print(f"The result of dividing {num1} by {num2} is: {result}")