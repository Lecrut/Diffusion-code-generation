def convert_distance(value, source_unit):
    if not isinstance(value, (int, float)):
        raise TypeError("Value must be a number")
    if isinstance(value, bool):
        raise TypeError("Value must be a number")
    if not isinstance(source_unit, str):
        raise TypeError("Source unit must be a string")
    
    source_unit_lower = source_unit.lower()
    
    if source_unit_lower not in ('meters', 'kilometers', 'miles', 'feet'):
        raise ValueError("Invalid source unit. Use 'meters', 'kilometers', 'miles', or 'feet'")
    
    to_meters = {
        'meters': 1.0,
        'kilometers': 1000.0,
        'miles': 1609.344,
        'feet': 0.3048
    }
    
    from_meters = {
        'meters': 1.0,
        'kilometers': 1.0 / 1000.0,
        'miles': 1.0 / 1609.344,
        'feet': 1.0 / 0.3048
    }
    
    distance_in_meters = value * to_meters[source_unit_lower]
    
    results = {}
    for unit in ('meters', 'kilometers', 'miles', 'feet'):
        results[unit] = round(distance_in_meters * from_meters[unit], 6)
    
    return results

if __name__ == '__main__':
    result1 = convert_distance(1.0, 'meters')
    print(result1)
    
    result2 = convert_distance(5.0, 'kilometers')
    print(result2)
    
    result3 = convert_distance(10.0, 'miles')
    print(result3)
    
    result4 = convert_distance(100.0, 'feet')
    print(result4)