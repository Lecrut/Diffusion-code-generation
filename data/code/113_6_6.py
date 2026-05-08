def subtract_and_check(a, b):
    result = a - b
    if result < 0:
        raise ValueError("Subtraction resulted in a negative number")
    return result
if __name__ == '__main__':
    num1 = 100
    num2 = 30
    try:
        result1 = subtract_and_check(num1, num2)
        print(f"Result of {num1} - {num2}: {result1}")
    except ValueError as e:
        print(f"Error: {e}")
    num3 = 50
    num4 = 150
    try:
        result2 = subtract_and_check(num3, num4)
        print(f"Result of {num3} - {num4}: {result2}")
    except ValueError as e:
        print(f"Error: {e}")
    num5 = 75
    num6 = 25
    try:
        result3 = subtract_and_check(num5, num6)
        print(f"Result of {num5} - {num6}: {result3}")
    except ValueError as e:
        print(f"Error: {e}")