def calculate_length_ratio(length1, length2):
    if length2 == 0:
        raise ValueError("length2 must not be zero to avoid division by zero.")
    return length1 / length2

if __name__ == '__main__':
    length1 = 15.5
    length2 = 3.1
    ratio = calculate_length_ratio(length1, length2)
    print(ratio)