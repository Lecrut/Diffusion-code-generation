def convert_distance(value: float, source_unit: str) -> float:
    valid_units = ('meters', 'kilometers', 'miles', 'feet', 'm', 'km', 'mi', 'ft')
    if source_unit not in valid_units:
        raise ValueError(f"Invalid unit: {source_unit}")
    
    if not isinstance(value, (int, float)):
        raise TypeError("Value must be a number")
    
    unit_map = {
        'meters': 1.0,
        'm': 1.0,
        'kilometers': 1000.0,
        'km': 1000.0,
        'miles': 1609.344,
        'mi': 1609.344,
        'feet': 0.3048,
        'ft': 0.3048
    }
    
    meters = value * unit_map[source_unit]
    return round(meters, 6)

if __name__ == '__main__':
    result = convert_distance(1, 'miles')
    print(result)
    
    result2 = convert_distance(5280, 'feet')
    print(result2)
    
    result3 = convert_distance(1, 'km')
    print(result3)