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
        raise ValueError(f"Unsupported unit: {source_unit}")
    
    meters = value * conversion_factors[source_unit]
    
    conversions = {
        'meters': meters,
        'kilometers': meters / 1000.0,
        'miles': meters / 1609.344,
        'feet': meters / 0.3048
    }
    
    return {unit: round(converted, 6) for unit, converted in conversions.items()}

if __name__ == '__main__':
    sample_values = [
        (10, 'meters'),
        (5, 'kilometers'),
        (2, 'miles'),
        (3048, 'feet')
    ]
    
    for value, unit in sample_values:
        print(convert_distance(value, unit))