def compare_lengths(value1, unit1, value2, unit2):
    conversions = {
        'in': 2.54,
        'cm': 1.0,
        'mm': 0.1,
        'ft': 30.48,
        'm': 100.0,
    }
    factor1 = conversions[unit1.lower()]
    factor2 = conversions[unit2.lower()]
    cm1 = value1 * factor1
    cm2 = value2 * factor2
    if cm1 > cm2:
        return f"{value1} {unit1} is longer than {value2} {unit2}"
    elif cm2 > cm1:
        return f"{value2} {unit2} is longer than {value1} {unit1}"
    else:
        return f"{value1} {unit1} and {value2} {unit2} are equal"

if __name__ == '__main__':
    result = compare_lengths(10, 'in', 25, 'cm')
    print(result)