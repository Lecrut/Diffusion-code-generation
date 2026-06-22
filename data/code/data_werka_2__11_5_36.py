def calculate_ratio(length1, length2):
    if length1 <= 0 or length2 <= 0:
        raise ValueError("Both lengths must be positive")
    return length1 / length2

if __name__ == '__main__':
    LENGTH1 = 15
    LENGTH2 = 3
    try:
        ratio = calculate_ratio(LENGTH1, LENGTH2)
        print(ratio)
    except ValueError as e:
        print(e)