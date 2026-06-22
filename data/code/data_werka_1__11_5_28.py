def calculate_ratio(length1, length2):
    if length1 <= 0 or length2 <= 0:
        raise ValueError("Both lengths must be positive.")
    return length1 / length2

if __name__ == '__main__':
    length_a = 15
    length_b = 5
    ratio = calculate_ratio(length_a, length_b)
    print(ratio)