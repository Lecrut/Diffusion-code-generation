def compare_lengths(length1_in_inches, length2_in_cm):
    INCH_TO_CM = 2.54
    length1_in_cm = length1_in_inches * INCH_TO_CM
    if length1_in_cm > length2_in_cm:
        return 'Length in inches is greater.'
    elif length1_in_cm < length2_in_cm:
        return 'Length in centimeters is greater.'
    else:
        return 'Both lengths are equal.'
if __name__ == '__main__':
    length1 = 10
    length2 = 25.4
    result = compare_lengths(length1, length2)
    print(result)