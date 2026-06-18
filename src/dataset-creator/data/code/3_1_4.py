def divide_two_numbers(a, b):
    try:
        result = a / b
        return result
    except TypeError:
        raise ValueError("Both inputs must be numeric.")
    except ZeroDivisionError:
        raise ZeroDivisionError("Cannot divide by zero.")
if __name__ == '__main__':
    num1 = 10.5
    num2 = 2.0
    print(f"Result of {num1} / {num2}: {divide_two_numbers(num1, num2)}")
    num3 = 7.0
    num4 = 3.0
    print(f"Result of {num3} / {num4}: {divide_two_numbers(num3, num4)}")
    try:
        divide_two_numbers(5.0, 0.0)
    except ZeroDivisionError as e:
        print(f"Caught expected error for division by zero: {e}")
    try:
        divide_two_numbers("a", 2.0)
    except ValueError as e:
        print(f"Caught expected error for non-numeric input: {e}")