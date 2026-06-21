def compare_lengths(length1_in_inches, length2_in_cm):
    INCH_TO_CM = 2.54
    length1_in_cm = length1_in_inches * INCH_TO_CM
    if length1_in_cm > length2_in_cm:
        return 'Length 1 is greater than Length 2'
    elif length1_in_cm < length2_in_cm:
        return 'Length 1 is less than Length 2'
    else:
        return 'Both lengths are equal'
if __name__ == '__main__':
    length1 = 5
    length2 = 10
    result = compare_lengths(length1, length2)
    print(result)