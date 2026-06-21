def calculate_length_ratio(length1, length2):
    EPSILON = 1e-9
    if abs(length2) < EPSILON:
        raise ValueError("length2 is too close to zero for division.")
    return length1 / length2

if __name__ == '__main__':
    LENGTH1 = 20.75
    LENGTH2 = 4.5
    ratio = calculate_length_ratio(LENGTH1, LENGTH2)
    print(ratio)