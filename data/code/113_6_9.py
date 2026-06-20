def subtract_numbers(a, b):
    if not (isinstance(a, (int, float)) and isinstance(b, (int, float))):
        raise TypeError("Both inputs must be numbers")
    return a - b

if __name__ == '__main__':
    num1 = 100
    num2 = 45
    try:
        result1 = subtract_numbers(num1, num2)
        print(f"Result of {num1} - {num2}: {result1}")
    except TypeError as e:
        print(f"Error: {e}")

    num3 = 'a'
    num4 = 20
    try:
        result2 = subtract_numbers(num3, num4)
        print(f"Result of {num3} - {num4}: {result2}")
    except TypeError as e:
        print(f"Error: {e}")