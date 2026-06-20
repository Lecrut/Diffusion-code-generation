def subtract_and_check(a, b):
    if not isinstance(a, (int, float)) or not isinstance(b, (int, float)):
        raise TypeError("Both inputs must be numbers")
    result = a - b
    if result < 0:
        raise ValueError("Subtraction resulted in a negative number")
    return result

if __name__ == '__main__':
    num1 = 150
    num2 = 75
    try:
        result1 = subtract_and_check(num1, num2)
        print(f"Result of {num1} - {num2}: {result1}")
    except (TypeError, ValueError) as e:
        print(f"Error: {e}")

    num3 = 50.5
    num4 = 20.75
    try:
        result2 = subtract_and_check(num3, num4)
        print(f"Result of {num3} - {num4}: {result2}")
    except (TypeError, ValueError) as e:
        print(f"Error: {e}")

    num5 = '100'
    num6 = 50
    try:
        result3 = subtract_and_check(num5, num6)
        print(f"Result of {num5} - {num6}: {result3}")
    except (TypeError, ValueError) as e:
        print(f"Error: {e}")