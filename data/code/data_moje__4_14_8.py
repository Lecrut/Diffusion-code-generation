def convert_distance(value, from_unit):
    valid_units = ('m', 'km', 'mi', 'ft')
    if not isinstance(value, (int, float)):
        raise TypeError("Value must be a number")
    if isinstance(value, bool):
        raise TypeError("Value must be a number")
    if from_unit not in valid_units:
        raise ValueError("Invalid unit. Must be one of: m, km, mi, ft")
    
    conversion_to_meters = {
        'm': 1.0,
        'km': 1000.0,
        'mi': 1609.344,
        'ft': 0.3048
    }
    
    meters = value * conversion_to_meters[from_unit]
    
    results = {
        'm': meters,
        'km': meters / 1000.0,
        'mi': meters / 1609.344,
        'ft': meters / 0.3048
    }
    
    converted_values = {unit: round(val, 6) for unit, val in results.items()}
    
    return converted_values

if __name__ == '__main__':
    result = convert_distance(1, 'mi')
    print(result)
    result2 = convert_distance(1000, 'm')
    print(result2)
    result3 = convert_distance(5280, 'ft')
    print(result3)
    result4 = convert_distance(10, 'km')
    print(result4)