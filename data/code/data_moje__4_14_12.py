def convert_distance(value, unit):
    if not isinstance(value, (int, float)):
        raise TypeError("Value must be a number")
    if not isinstance(unit, str):
        raise TypeError("Unit must be a string")
    
    unit_lower = unit.strip().lower()
    
    if unit_lower == 'm':
        meters = value
    elif unit_lower == 'km':
        meters = value * 1000
    elif unit_lower == 'mi':
        meters = value * 1609.344
    elif unit_lower == 'ft':
        meters = value * 0.3048
    else:
        raise ValueError(f"Unsupported unit: {unit}")
    
    return round(meters, 6)

if __name__ == '__main__':
    result1 = convert_distance(1, 'km')
    print(result1)
    
    result2 = convert_distance(1, 'mi')
    print(result2)
    
    result3 = convert_distance(1, 'ft')
    print(result3)
    
    result4 = convert_distance(500, 'm')
    print(result4)