def calculate_length_ratio(length1, length2):
    min_length = min(length1, length2)
    max_length = max(length1, length2)
    ratio = max_length / min_length
    return ratio

if __name__ == '__main__':
    LENGTH_A = 7
    LENGTH_B = 28
    ratio = calculate_length_ratio(LENGTH_A, LENGTH_B)
    print(ratio)