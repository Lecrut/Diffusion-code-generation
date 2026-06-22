def convert_distance(value, source_unit):
    conversion_factors = {
        'm': 1.0,
        'km': 1000.0,
        'mi': 1609.344,
        'ft': 0.3048
    }
    
    source_unit_lower = source_unit.lower()
    
    if source_unit_lower not in conversion_factors:
        raise ValueError(f"Invalid source unit: {source_unit}")
    
    if not isinstance(value, (int, float)):
        raise TypeError("Value must be a numeric type")
    
    if isinstance(value, bool):
        raise TypeError("Boolean values are not accepted as numeric input")
    
    if value < 0:
        raise ValueError("Distance cannot be negative")
    
    meters = value * conversion_factors[source_unit_lower]
    return round(meters, 6)

if __name__ == '__main__':
    print(convert_distance(1.0, 'km'))
    print(convert_distance(1.0, 'mi'))
    print(convert_distance(5280.0, 'ft'))
    print(convert_distance(1000.0, 'm'))