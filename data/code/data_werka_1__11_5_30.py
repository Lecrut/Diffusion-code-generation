def calculate_ratio(length1, length2):
    if length1 <= 0 or length2 <= 0:
        raise ValueError("Both lengths must be positive.")
    return length1 / length2

if __name__ == '__main__':
    sample_length1 = 10
    sample_length2 = 5
    ratio = calculate_ratio(sample_length1, sample_length2)
    print(ratio)