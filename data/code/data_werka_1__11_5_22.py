def calculate_ratio(length1, length2):
    if length1 <= 0 or length2 <= 0:
        raise ValueError("Both lengths must be positive numbers.")
    return length1 / length2

if __name__ == '__main__':
    try:
        ratio = calculate_ratio(10, 5)
        print(ratio)
    except ValueError as e:
        print(e)