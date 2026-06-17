def divide_two_numbers(a, b):
    if b == 0:
        raise ZeroDivisionError("Cannot divide by zero")
    return a / b
if __name__ == '__main__':
    num1 = 10.0
    num2 = 2.0
    try:
        result = divide_two_numbers(num1, num2)
        print(f"Result of {num1} / {num2}: {result}")
    except ZeroDivisionError as e:
        print(f"Error: {e}")
    num3 = 15.0
    num4 = 0.0
    try:
        result = divide_two_numbers(num3, num4)
        print(f"Result of {num3} / {num4}: {result}")
    except ZeroDivisionError as e:
        print(f"Error: {e}")