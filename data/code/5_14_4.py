def compare_lengths(value1, unit1, value2, unit2):
    inch_to_cm = 2.54
    if unit1 == 'inches':
        normalized1 = value1 * inch_to_cm
    else:
        normalized1 = value1
    
    if unit2 == 'inches':
        normalized2 = value2 * inch_to_cm
    else:
        normalized2 = value2
    
    if normalized1 > normalized2:
        return f"{value1} {unit1} is greater than {value2} {unit2}"
    elif normalized1 < normalized2:
        return f"{value1} {unit1} is less than {value2} {unit2}"
    else:
        return f"{value1} {unit1} is equal to {value2} {unit2}"

if __name__ == '__main__':
    result = compare_lengths(10, 'inches', 25.4, 'centimeters')
    print(result)
    result2 = compare_lengths(5, 'inches', 10, 'centimeters')
    print(result2)
    result3 = compare_lengths(100, 'centimeters', 40, 'inches')
    print(result3)