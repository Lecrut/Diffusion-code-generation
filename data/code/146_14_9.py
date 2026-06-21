def divide_numbers(a, b):
    try:
        result = a / b
    except ZeroDivisionError:
        print("Error: Division by zero is not allowed.")
        return None
    else:
        return result

if __name__ == '__main__':
    num1 = 10
    num2 = 0
    result = divide_numbers(num1, num2)
    if result is not None:
        print(f"The result of {num1} / {num2} is {result}")