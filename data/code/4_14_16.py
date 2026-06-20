def convert_distance(value, from_unit):
    if not isinstance(value, (int, float)):
        raise TypeError("Value must be a number")
    if isinstance(value, bool):
        raise TypeError("Value must be a number")
    if not isinstance(from_unit, str):
        raise TypeError("Unit must be a string")
    
    from_unit = from_unit.lower().strip()
    
    if from_unit not in ('meters', 'kilometers', 'miles', 'feet'):
        raise ValueError("Invalid unit. Use meters, kilometers, miles, or feet")
    
    if value < 0:
        raise ValueError("Distance cannot be negative")
    
    to_meters = {
        'meters': 1.0,
        'kilometers': 1000.0,
        'miles': 1609.344,
        'feet': 0.3048
    }
    
    from_meters = {
        'meters': 1.0,
        'kilometers': 1000.0,
        'miles': 1609.344,
        'feet': 0.3048
    }
    
    value_in_meters = value * from_meters[from_unit]
    
    results = {}
    results['meters'] = round(value_in_meters / to_meters['meters'], 6)
    results['kilometers'] = round(value_in_meters / to_meters['kilometers'], 6)
    results['miles'] = round(value_in_meters / to_meters['miles'], 6)
    results['feet'] = round(value_in_meters / to_meters['feet'], 6)
    
    return results

if __name__ == '__main__':
    result = convert_distance(1, 'miles')
    print(result)
    
    result2 = convert_distance(100, 'meters')
    print(result2)
    
    result3 = convert_distance(5280, 'feet')
    print(result3)