def convert_distance(value, source_unit):
    conversion_factors = {
        'meters': 1.0,
        'kilometers': 1000.0,
        'miles': 1609.344,
        'feet': 0.3048
    }
    
    if not isinstance(value, (int, float)):
        raise ValueError("Value must be a numeric type.")
    
    if source_unit not in conversion_factors:
        raise ValueError("Invalid source unit. Supported units are: meters, kilometers, miles, feet.")
    
    base_value = value * conversion_factors[source_unit]
    
    converted_values = {
        'meters': base_value / conversion_factors['meters'],
        'kilometers': base_value / conversion_factors['kilometers'],
        'miles': base_value / conversion_factors['miles'],
        'feet': base_value / conversion_factors['feet']
    }
    
    return {unit: round(value, 6) for unit, value in converted_values.items()}

if __name__ == '__main__':
    sample_value = 10
    sample_unit = 'kilometers'
    result = convert_distance(sample_value, sample_unit)
    print(result)