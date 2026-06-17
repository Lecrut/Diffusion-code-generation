def divide_numbers(a, b):
    try:
        result = a / b
        return result
    except ZeroDivisionError:
        return "Error: Cannot divide by zero."
    except TypeError:
        return "Error: Invalid input. Please enter numbers."
if __name__ == '__main__':
    num1 = 20
    num2 = 4
    result = divide_numbers(num1, num2)
    print(result)