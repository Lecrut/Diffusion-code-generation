def subtract_and_check(a, b):
    result = a - b
    if result < 0:
        raise ValueError("Subtraction resulted in a negative number")
    return result
if __name__ == '__main__':
    a1 = 100
    b1 = 30
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
    a3 = 200
    b3 = 100
    try:
        result3 = subtract_and_check(a3, b3)
        print(f"Result of {a3} - {b3}: {result3}")
    except ValueError as e:
        print(f"Error: {e}")