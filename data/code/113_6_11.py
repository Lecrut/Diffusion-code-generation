def subtract_and_check(a, b):
    if not all(isinstance(x, (int, float)) for x in [a, b]):
        raise TypeError("Both inputs must be numbers")
    result = a - b
    if result < 0:
        raise ValueError("Subtraction resulted in a negative number")
    return result

if __name__ == '__main__':
    a1 = 100
    b1 = 45
    try:
        result1 = subtract_and_check(a1, b1)
        print(f"Result of {a1} - {b1}: {result1}")
    except ValueError as e:
        print(f"Error: {e}")

    a2 = 50
    b2 = 150
    try:
        result2 = subtract_and_check(a2, b2)
        print(f"Result of {a2} - {b2}: {result2}")
    except ValueError as e:
        print(f"Error: {e}")