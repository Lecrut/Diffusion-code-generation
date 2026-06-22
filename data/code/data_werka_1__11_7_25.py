def calculate_length_ratio(length1, length2):
    if length2 == 0:
        raise ValueError("length2 cannot be zero")
    return length1 / length2

if __name__ == '__main__':
    length1 = 10.5
    length2 = 3.5
    ratio = calculate_length_ratio(length1, length2)
    print(ratio)