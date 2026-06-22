def calculate_ratio(length1, length2):
    if length1 <= 0 or length2 <= 0:
        raise ValueError("Both lengths must be positive numbers.")
    return length1 / length2

if __name__ == '__main__':
    length1 = 15.0
    length2 = 5.0
    ratio = calculate_ratio(length1, length2)
    print(ratio)