def calculate_length_ratio(length1, length2):
    if length2 == 0:
        raise ValueError("length2 cannot be zero")
    return length1 / length2

if __name__ == '__main__':
    LENGTH1 = 7.85
    LENGTH2 = 2.34
    try:
        ratio = calculate_length_ratio(LENGTH1, LENGTH2)
        print(ratio)
    except ValueError as e:
        print(e)