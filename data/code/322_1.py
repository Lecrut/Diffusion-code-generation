def divide_two_numbers(a, b):
    if b == 0:
        raise ZeroDivisionError("Cannot divide by zero")
    return a / b
if __name__ == '__main__':
    num1 = 10.0
    num2 = 2.0
    print(f"Result of {num1} / {num2}: {divide_two_numbers(num1, num2)}")
    num3 = 15.0
    num4 = 3.0
    print(f"Result of {num3} / {num4}: {divide_two_numbers(num3, num4)}")
    try:
        num5 = 10.0
        num6 = 0.0
        result = divide_two_numbers(num5, num6)
        print(f"Result of {num5} / {num6}: {result}")
    except ZeroDivisionError as e:
        print(f"Caught exception: {e}")