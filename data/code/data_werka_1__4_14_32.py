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
        raise ValueError("Invalid source unit. Use 'm', 'km', 'mi', or 'ft'.")
    
    meters = value * conversion_factors[source_unit]
    
    converted_distances = {
        'm': meters,
        'km': meters / 1000.0,
        'mi': meters / 1609.344,
        'ft': meters / 0.3048
    }
    
    return {unit: round(distance, 6) for unit, distance in converted_distances.items()}

if __name__ == '__main__':
    sample_values = [
        (10, 'm'),
        (5, 'km'),
        (2, 'mi'),
        (300, 'ft')
    ]
    
    for value, source_unit in sample_values:
        result = convert_distance(value, source_unit)
        print(f"Original: {value} {source_unit}")
        for unit, distance in result.items():
            print(f"Converted to {unit}: {distance}")