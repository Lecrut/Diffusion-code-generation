def convert_distance(value, from_unit, to_unit):
    conversions = {
        ('m', 'km'): 1000,
        ('m', 'mi'): 0.000621371,
        ('km', 'm'): 0.001,
        ('km', 'mi'): 0.000621371 / 0.001,
        ('mi', 'm'): 1 / 0.000621371,
        ('mi', 'km'): 1 / (0.000621371 / 0.001),
    }
    
    units_map = {
        'meters': 'm',
        'kilometers': 'km',
        'miles': 'mi'
    }
    
    normalized_from = units_map.get(from_unit.lower())
    normalized_to = units_map.get(to_unit.lower())
    
    if normalized_from is None or normalized_to is None:
        raise ValueError("Invalid unit specified")
    
    if normalized_from == normalized_to:
        return value
    
    key = (normalized_from, normalized_to)
    if key not in conversions:
        raise ValueError("Conversion not supported")
    
    factor = conversions[key]
    result = value * factor
    return result

if __name__ == '__main__':
    result = convert_distance(1, 'kilometers', 'miles')
    print(result)
    
    result2 = convert_distance(1, 'miles', 'kilometers')
    print(result2)
    
    result3 = convert_distance(1, 'meters', 'kilometers')
    print(result3)