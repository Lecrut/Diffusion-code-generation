def calculate_length_ratio(length1, length2):
    min_length = min(length1, length2)
    max_length = max(length1, length2)
    ratio = max_length / min_length
    return ratio

if __name__ == '__main__':
    length_a = 10
    length_b = 25
    ratio = calculate_length_ratio(length_a, length_b)
    print(ratio)