def calculate_ratio(length1, length2):
    if length1 <= 0 or length2 <= 0:
        raise ValueError("Both lengths must be positive")
    return length1 / length2
if __name__ == '__main__':
    a = 10
    b = 5
    try:
        result = calculate_ratio(a, b)
        print(result)
    except ValueError as e:
        print(f"Error: {e}")
    a = 0
    b = 5
    try:
        result = calculate_ratio(a, b)
        print(result)
    except ValueError as e:
        print(f"Error: {e}")
    a = 10
    b = -5
    try:
        result = calculate_ratio(a, b)
        print(result)
    except ValueError as e:
        print(f"Error: {e}")