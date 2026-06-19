def calculate_ratio(length1, length2):
    if length1 <= 0 or length2 <= 0:
        raise ValueError("Both lengths must be positive.")
    return length1 / length2

if __name__ == '__main__':
    length1 = 10
    length2 = 5
    ratio = calculate_ratio(length1, length2)
    print(ratio)