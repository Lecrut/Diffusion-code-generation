def normalize_and_compare(length1, unit1, length2, unit2):
    if unit1 == 'inches' and unit2 == 'centimeters':
        normalized_length1 = length1 * 2.54
        comparison_result = normalized_length1 > length2
    elif unit1 == 'centimeters' and unit2 == 'inches':
        normalized_length2 = length2 * 2.54
        comparison_result = length1 > normalized_length2
    else:
        raise ValueError('Unsupported units for comparison')
    return comparison_result
if __name__ == '__main__':
    length1 = 10
    unit1 = 'inches'
    length2 = 25
    unit2 = 'centimeters'
    result = normalize_and_compare(length1, unit1, length2, unit2)
    print(result)