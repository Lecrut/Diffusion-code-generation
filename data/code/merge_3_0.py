def divide_numbers(a, b):
    try:
        result = a / b
        return result
    except ZeroDivisionError:
        return "Error: Cannot divide by zero."
    except TypeError:
        return "Error: Invalid input. Please enter numbers."
if __name__ == '__main__':
    num1 = 10
    num2 = 2
    result = divide_numbers(num1, num2)
    print(f"The result of dividing {num1} by {num2} is: {result}")
    num3 = 15
    num4 = 0
    result2 = divide_numbers(num3, num4)
    print(f"The result of dividing {num3} by {num4} is: {result2}")
    num5 = 8.5
    num6 = 2
    result3 = divide_numbers(num5, num6)
    print(f"The result of dividing {num5} by {num6} is: {result3}")