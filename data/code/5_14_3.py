def compare_lengths(length1, unit1, length2, unit2):
    conversion_factors = {
        'inches': 1.0,
        'centimeters': 2.54
    }
    
    if unit1 not in conversion_factors or unit2 not in conversion_factors:
        raise ValueError("Unsupported unit provided")
    
    normalized_length1 = length1 * conversion_factors[unit1]
    normalized_length2 = length2 * conversion_factors[unit2]
    
    if normalized_length1 > normalized_length2:
        return "First length is greater"
    elif normalized_length1 < normalized_length2:
        return "Second length is greater"
    else:
        return "Lengths are equal"

if __name__ == '__main__':
    result = compare_lengths(10, 'inches', 25.4, 'centimeters')
    print(result)