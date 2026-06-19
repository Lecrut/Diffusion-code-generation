def convert_distance(value, source_unit):
    conversion_factors = {
        'm': 1.0,
        'km': 1000.0,
        'mi': 1609.344,
        'ft': 0.3048
    }
    
    if not isinstance(value, (int, float)):
        raise ValueError("Value must be a numeric type.")
    
    if source_unit not in conversion_factors:
        raise ValueError("Invalid source unit. Supported units are: m, km, mi, ft.")
    
    meters = value * conversion_factors[source_unit]
    
    converted_values = {
        'm': meters / conversion_factors['m'],
        'km': meters / conversion_factors['km'],
        'mi': meters / conversion_factors['mi'],
        'ft': meters / conversion_factors['ft']
    }
    
    return {unit: round(distance, 6) for unit, distance in converted_values.items()}

if __name__ == '__main__':
    sample_value = 10
    sample_unit = 'km'
    result = convert_distance(sample_value, sample_unit)
    print(result)