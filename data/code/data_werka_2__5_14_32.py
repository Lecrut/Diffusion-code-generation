def compare_lengths(length1_inches, length2_cm):
    INCH_TO_CM = 2.54
    length1_cm = length1_inches * INCH_TO_CM
    if length1_cm > length2_cm:
        return f'{length1_inches} inches is longer than {length2_cm} cm.'
    elif length1_cm < length2_cm:
        return f'{length1_inches} inches is shorter than {length2_cm} cm.'
    else:
        return f'{length1_inches} inches is equal to {length2_cm} cm.'
if __name__ == '__main__':
    length1 = 10
    length2 = 25.4
    result = compare_lengths(length1, length2)
    print(result)