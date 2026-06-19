def calculate_length_ratio(length1, length2):
    if length2 == 0:
        raise ValueError("length2 cannot be zero")
    return length1 / length2

if __name__ == '__main__':
    sample_length1 = 15.5
    sample_length2 = 3.1
    ratio = calculate_length_ratio(sample_length1, sample_length2)
    print(ratio)