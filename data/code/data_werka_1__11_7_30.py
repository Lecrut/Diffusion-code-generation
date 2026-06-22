def calculate_length_ratio(length1, length2):
    if length2 == 0:
        raise ValueError("length2 cannot be zero for division.")
    return length1 / length2

if __name__ == '__main__':
    length1 = 15.75
    length2 = 3.5
    ratio = calculate_length_ratio(length1, length2)
    print(ratio)