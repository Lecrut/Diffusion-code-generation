def compare_lengths(length1_in, unit1, length2_in, unit2):
    cm_per_inch = 2.54
    if unit1 == 'inches':
        length1_cm = length1_in * cm_per_inch
    elif unit1 == 'cm':
        length1_cm = length1_in
    else:
        raise ValueError("Unsupported unit1")
    
    if unit2 == 'inches':
        length2_cm = length2_in * cm_per_inch
    elif unit2 == 'cm':
        length2_cm = length2_in
    else:
        raise ValueError("Unsupported unit2")
    
    if length1_cm > length2_cm:
        result = "Greater"
    elif length1_cm < length2_cm:
        result = "Less"
    else:
        result = "Equal"
    
    return result

if __name__ == '__main__':
    length1 = 12
    unit1 = 'inches'
    length2 = 30
    unit2 = 'cm'
    
    result = compare_lengths(length1, unit1, length2, unit2)
    print(result)