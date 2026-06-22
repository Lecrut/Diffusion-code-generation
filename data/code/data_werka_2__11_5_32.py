def calculate_ratio(length1, length2):
    if length1 <= 0 or length2 <= 0:
        raise ValueError("Both lengths must be positive")
    return length1 / length2

if __name__ == '__main__':
    SAMPLE_LENGTH1 = 20
    SAMPLE_LENGTH2 = 4
    try:
        ratio = calculate_ratio(SAMPLE_LENGTH1, SAMPLE_LENGTH2)
        print(ratio)
    except ValueError as e:
        print(e)