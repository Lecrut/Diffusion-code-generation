def compare_lengths(length1, unit1, length2, unit2):
    cm_to_inch = 0.393701
    inch_to_cm = 2.54
    if unit1 == 'inches':
        length1_cm = length1 * inch_to_cm
    elif unit1 == 'centimeters':
        length1_cm = length1
    else:
        raise ValueError('Unsupported unit for length1')
    if unit2 == 'inches':
        length2_cm = length2 * inch_to_cm
    elif unit2 == 'centimeters':
        length2_cm = length2
    else:
        raise ValueError('Unsupported unit for length2')
    if length1_cm > length2_cm:
        return 'Length 1 is greater than Length 2'
    elif length1_cm < length2_cm:
        return 'Length 1 is less than Length 2'
    else:
        return 'Length 1 is equal to Length 2'
if __name__ == '__main__':
    length1 = 10
    unit1 = 'inches'
    length2 = 25.4
    unit2 = 'centimeters'
    result = compare_lengths(length1, unit1, length2, unit2)
    print(result)