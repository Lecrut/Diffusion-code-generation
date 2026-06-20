def convert_length(value, from_unit, to_unit):
    conversion_factors = {
        'mm': 0.001,
        'cm': 0.01,
        'm': 1.0,
        'km': 1000.0,
        'in': 0.0254,
        'ft': 0.3048,
        'yd': 0.9144,
        'mi': 1609.344
    }
    
    from_unit_lower = from_unit.lower()
    to_unit_lower = to_unit.lower()
    
    if from_unit_lower not in conversion_factors:
        raise ValueError(f"Unsupported source unit: {from_unit}")
    if to_unit_lower not in conversion_factors:
        raise ValueError(f"Unsupported target unit: {to_unit}")
    
    meters = value * conversion_factors[from_unit_lower]
    result = meters / conversion_factors[to_unit_lower]
    
    return result

if __name__ == '__main__':
    sample_value = 100
    sample_from = 'cm'
    sample_to = 'in'
    result = convert_length(sample_value, sample_from, sample_to)
    print(result)
    
    sample_value2 = 5
    sample_from2 = 'km'
    sample_to2 = 'mi'
    result2 = convert_length(sample_value2, sample_from2, sample_to2)
    print(result2)
    
    sample_value3 = 72
    sample_from3 = 'in'
    sample_to3 = 'cm'
    result3 = convert_length(sample_value3, sample_from3, sample_to3)
    print(result3)