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
        raise ValueError(f"Unsupported unit: {source_unit}. Supported units are: m, km, mi, ft.")
    
    meters = value * conversion_factors[source_unit]
    
    return {
        'm': meters,
        'km': meters / 1000.0,
        'mi': meters / 1609.344,
        'ft': meters / 0.3048
    }

if __name__ == '__main__':
    sample_values = [
        (10, 'm'),
        (5, 'km'),
        (2, 'mi'),
        (300, 'ft')
    ]
    
    for value, unit in sample_values:
        converted = convert_distance(value, unit)
        print(f"{value} {unit} is equivalent to:")
        for target_unit, distance in converted.items():
            print(f"  {distance:.6f} {target_unit}")