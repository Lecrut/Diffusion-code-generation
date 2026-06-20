def calculate_length_ratio(length1, length2):
    smaller = min(length1, length2)
    larger = max(length1, length2)
    return larger / smaller

if __name__ == '__main__':
    length_a = 10
    length_b = 25
    ratio = calculate_length_ratio(length_a, length_b)
    print(ratio)