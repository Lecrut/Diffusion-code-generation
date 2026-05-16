def subtract_and_check(a, b):
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
    a2 = 10
    b2 = 25
    try:
        result2 = subtract_and_check(a2, b2)
        print(f"Result of {a2} - {b2}: {result2}")
    except ValueError as e:
        print(f"Error: {e}")
    a3 = 50
    b3 = 50
    try:
        result3 = subtract_and_check(a3, b3)
        print(f"Result of {a3} - {b3}: {result3}")
    except ValueError as e:
        print(f"Error: {e}")
    a4 = 10
    b4 = 50
    try:
        result4 = subtract_and_check(a4, b4)
        print(f"Result of {a4} - {b4}: {result4}")
    except ValueError as e:
        print(f"Error: {e}")