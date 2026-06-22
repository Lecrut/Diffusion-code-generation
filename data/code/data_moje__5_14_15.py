def compare_lengths(value1, unit1, value2, unit2):
    conversion_to_cm = {
        'inches': 2.54,
        'cm': 1.0,
        'centimeters': 1.0,
        'meters': 100.0,
        'feet': 30.48,
    }
    value1_cm = value1 * conversion_to_cm[unit1]
    value2_cm = value2 * conversion_to_cm[unit2]
    if value1_cm > value2_cm:
        return f"{value1} {unit1} is longer than {value2} {unit2}"
    elif value2_cm > value1_cm:
        return f"{value2} {unit2} is longer than {value1} {unit1}"
    else:
        return f"{value1} {unit1} is equal to {value2} {unit2}"

if __name__ == '__main__':
    result = compare_lengths(10, 'inches', 25, 'cm')
    print(result)