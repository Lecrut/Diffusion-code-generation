def normalize_and_compare(length1, unit1, length2, unit2):
    if unit1 == 'inches':
        length1_cm = length1 * 2.54
    elif unit1 == 'centimeters':
        length1_cm = length1
    else:
        raise ValueError("Unsupported unit for length1")

    if unit2 == 'inches':
        length2_cm = length2 * 2.54
    elif unit2 == 'centimeters':
        length2_cm = length2
    else:
        raise ValueError("Unsupported unit for length2")

    if length1_cm > length2_cm:
        return f"{length1} {unit1} is longer than {length2} {unit2}"
    elif length1_cm < length2_cm:
        return f"{length1} {unit1} is shorter than {length2} {unit2}"
    else:
        return f"{length1} {unit1} is equal to {length2} {unit2}"

if __name__ == '__main__':
    length1 = 10
    unit1 = 'inches'
    length2 = 25.4
    unit2 = 'centimeters'

    result = normalize_and_compare(length1, unit1, length2, unit2)
    print(result)