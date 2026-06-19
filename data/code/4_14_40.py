def convert_distance(value, from_unit):
    conversion_factors = {
        'm': 1.0,
        'km': 1000.0,
        'mi': 1609.344,
        'ft': 0.3048
    }
    
    if not isinstance(value, (int, float)):
        raise ValueError("Value must be a numeric type.")
    
    if from_unit not in conversion_factors:
        raise ValueError("Invalid source unit. Supported units are: m, km, mi, ft.")
    
    meters = value * conversion_factors[from_unit]
    
    converted_values = {
        'm': meters,
        'km': meters / 1000.0,
        'mi': meters / 1609.344,
        'ft': meters / 0.3048
    }
    
    return {unit: round(converted_values[unit], 6) for unit in conversion_factors}

if __name__ == '__main__':
    sample_value = 5.0
    sample_unit = 'km'
    converted_distances = convert_distance(sample_value, sample_unit)
    print(converted_distances)