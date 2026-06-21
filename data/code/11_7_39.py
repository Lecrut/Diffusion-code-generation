def calculate_length_ratio(length1, length2):
    if length2 == 0:
        raise ValueError("length2 cannot be zero for division.")
    return length1 / length2

if __name__ == '__main__':
    sample_length1 = 25.6
    sample_length2 = 8.4
    try:
        ratio = calculate_length_ratio(sample_length1, sample_length2)
        print(ratio)
    except ValueError as e:
        print(e)