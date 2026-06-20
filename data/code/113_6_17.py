def subtract_and_check(a, b):
    if not isinstance(a, (int, float)) or not isinstance(b, (int, float)):
        raise TypeError("Both inputs must be numbers")
    result = a - b
    return result

if __name__ == '__main__':
    num1 = 100
    num2 = 45
    try:
        result1 = subtract_and_check(num1, num2)
        print(f"Result of {num1} - {num2}: {result1}")
    except TypeError as e:
        print(f"Error: {e}")

    num3 = 50
    num4 = 150
    try:
        result2 = subtract_and_check(num3, num4)
        print(f"Result of {num3} - {num4}: {result2}")
    except TypeError as e:
        print(f"Error: {e}")