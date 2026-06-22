def convert_distance(value, unit):
    if not isinstance(value, (int, float)):
        raise TypeError("Value must be a number")
    
    if not isinstance(unit, str):
        raise TypeError("Unit must be a string")
    
    unit_lower = unit.lower().strip()
    
    conversions = {
        'meters': 1.0,
        'm': 1.0,
        'kilometers': 1000.0,
        'km': 1000.0,
        'miles': 1609.344,
        'mi': 1609.344,
        'feet': 0.3048,
        'ft': 0.3048
    }
    
    if unit_lower not in conversions:
        raise ValueError(f"Unsupported unit: {unit}")
    
    meters = value * conversions[unit_lower]
    result = meters / conversions['meters']
    
    return round(result, 6)

if __name__ == '__main__':
    print(convert_distance(1, 'km'))
    print(convert_distance(1, 'miles'))
    print(convert_distance(1, 'feet'))
    print(convert_distance(5280, 'ft'))
    print(convert_distance(1000, 'm'))