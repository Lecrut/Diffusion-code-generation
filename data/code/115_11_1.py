def divide_two_numbers(a, b):
    if b == 0:
        raise ValueError("Cannot divide by zero")
    return a / b
if __name__ == '__main__':
    num1 = 10.0
    num2 = 2.0
    result1 = divide_two_numbers(num1, num2)
    print(f"Result of {num1} / {num2}: {result1}")
    num3 = 15.0
    num4 = 3.0
    result2 = divide_two_numbers(num3, num4)
    print(f"Result of {num3} / {num4}: {result2}")
    num5 = 7.0
    num6 = 0.0
    try:
        result3 = divide_two_numbers(num5, num6)
        print(f"Result of {num5} / {num6}: {result3}")
    except ValueError as e:
        print(f"Error caught: {e}")