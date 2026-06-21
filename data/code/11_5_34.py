def calculate_ratio(length1, length2):
    if not (isinstance(length1, (int, float)) and isinstance(length2, (int, float))):
        raise ValueError("Both lengths must be numbers")
    if length1 <= 0 or length2 <= 0:
        raise ValueError("Both lengths must be positive")
    return length1 / length2

if __name__ == '__main__':
    try:
        ratio = calculate_ratio(8, 4)
        print(ratio)
    except ValueError as e:
        print(e)