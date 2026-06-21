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
        raise ValueError(f"Unsupported source unit: {source_unit}")
    
    meters = value * conversion_factors[source_unit]
    
    converted_values = {
        'meters': meters,
        'kilometers': meters / 1000.0,
        'miles': meters / 1609.344,
        'feet': meters / 0.3048
    }
    
    return {unit: round(converted_values[unit], 6) for unit in conversion_factors}

if __name__ == '__main__':
    sample_value = 100
    sample_unit = 'meters'
    converted_distances = convert_distance(sample_value, sample_unit)
    print(converted_distances)