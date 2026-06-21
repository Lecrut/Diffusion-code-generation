def inches_to_cm(inches):
    return inches * 2.54

def compare_lengths(length1, unit1, length2, unit2):
    if unit1 == 'inches' and unit2 == 'cm':
        length1_cm = inches_to_cm(length1)
        comparison_result = length1_cm > length2
    elif unit1 == 'cm' and unit2 == 'inches':
        length2_cm = inches_to_cm(length2)
        comparison_result = length1 > length2_cm
    else:
        raise ValueError("Unsupported units. Please use 'inches' or 'cm'.")
    
    return comparison_result

if __name__ == '__main__':
    length1 = 5
    unit1 = 'inches'
    length2 = 10
    unit2 = 'cm'
    
    result = compare_lengths(length1, unit1, length2, unit2)
    print(result)