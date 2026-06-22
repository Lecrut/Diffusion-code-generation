def calculate_ratio(length1, length2):
    if length1 <= 0 or length2 <= 0:
        raise ValueError("Both lengths must be positive")
    return length1 / length2

if __name__ == '__main__':
    try:
        result = calculate_ratio(10, 5)
        print(result)
    except ValueError as e:
        print(e)