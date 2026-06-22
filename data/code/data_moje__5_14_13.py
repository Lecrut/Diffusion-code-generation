def convert_inches_to_cm(inches):
    return inches * 2.54

def compare_lengths(val1_unit, val1, val2_unit, val2):
    if val1_unit == 'inches':
        val1_cm = convert_inches_to_cm(val1)
    else:
        val1_cm = val1
    
    if val2_unit == 'inches':
        val2_cm = convert_inches_to_cm(val2)
    else:
        val2_cm = val2
        
    if val1_cm > val2_cm:
        return f"{val1} {val1_unit} is longer than {val2} {val2_unit}"
    elif val1_cm < val2_cm:
        return f"{val2} {val2_unit} is longer than {val1} {val1_unit}"
    else:
        return f"{val1} {val1_unit} is equal to {val2} {val2_unit}"

if __name__ == '__main__':
    result = compare_lengths('inches', 10, 'cm', 25)
    print(result)