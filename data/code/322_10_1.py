def divide_numbers(a, b):
    try:
        result = a / b
        return result
    except ZeroDivisionError:
        return "Error: Cannot divide by zero."
if __name__ == '__main__':
    num1 = 10
    num2 = 2
    result = divide_numbers(num1, num2)
    print(result)