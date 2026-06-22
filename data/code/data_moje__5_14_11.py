def compare_lengths(length_a_unit, value_a, length_b_unit, value_b):
    conversion_to_cm = {
        'inches': 2.54,
        'centimeters': 1.0
    }
    
    if length_a_unit not in conversion_to_cm or length_b_unit not in conversion_to_cm:
        raise ValueError("Unsupported unit")
        
    cm_a = value_a * conversion_to_cm[length_a_unit]
    cm_b = value_b * conversion_to_cm[length_b_unit]
    
    if cm_a > cm_b:
        return f"{value_a} {length_a_unit} is greater than {value_b} {length_b_unit}"
    elif cm_a < cm_b:
        return f"{value_a} {length_a_unit} is less than {value_b} {length_b_unit}"
    else:
        return f"{value_a} {length_a_unit} is equal to {value_b} {length_b_unit}"

if __name__ == '__main__':
    inches_val = 10
    centimeters_val = 25.4
    result = compare_lengths('inches', inches_val, 'centimeters', centimeters_val)
    print(result)