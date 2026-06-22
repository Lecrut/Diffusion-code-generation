def calculate_ratio(length1, length2):
    if length2 == 0:
        raise ValueError("Length2 cannot be zero for division.")
    return length1 / length2

if __name__ == '__main__':
    length1 = 123456789.123456789
    length2 = 987654321.987654321
    try:
        ratio = calculate_ratio(length1, length2)
        print(f"The ratio of the two lengths is: {ratio}")
    except ValueError as e:
        print(e)