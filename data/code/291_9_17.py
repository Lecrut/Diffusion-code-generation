def compare_lengths(length1, unit1, length2, unit2):
    conversion_factors = {
        'rod': 5.0292,
        'meter': 1
    }
    
    if unit1 not in conversion_factors or unit2 not in conversion_factors:
        raise ValueError("Invalid unit of measurement")
    
    length1_converted = length1 * conversion_factors[unit1]
    length2_converted = length2 * conversion_factors[unit2]
    
    return (length1_converted, length2_converted)

if __name__ == '__main__':
    result = compare_lengths(3, 'rod', 15.0876, 'meter')
    print(result)