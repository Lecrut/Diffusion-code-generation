def compare_lengths(length1_unit1, unit1, length2_unit2, unit2):
    conversion_factors = {'inches': 2.54, 'centimeters': 1.0}
    length1_cm = length1_unit1 * conversion_factors[unit1]
    length2_cm = length2_unit2 * conversion_factors[unit2]
    if length1_cm > length2_cm:
        return f'{length1_unit1} {unit1} is greater than {length2_unit2} {unit2}'
    elif length2_cm > length1_cm:
        return f'{length2_unit2} {unit2} is greater than {length1_unit1} {unit1}'
    else:
        return f'{length1_unit1} {unit1} is equal to {length2_unit2} {unit2}'
if __name__ == '__main__':
    result = compare_lengths(10, 'inches', 25, 'centimeters')
    print(result)