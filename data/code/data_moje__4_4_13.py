def convert_distance(distance, from_unit, to_unit):
    if not isinstance(distance, (int, float)):
        raise TypeError("Distance must be a number")
    
    units_to_base = {
        'meter': 1.0,
        'kilometer': 1000.0,
        'centimeter': 0.01,
        'millimeter': 0.001,
        'mile': 1609.344,
        'yard': 0.9144,
        'foot': 0.3048,
        'inch': 0.0254
    }
    
    if from_unit not in units_to_base:
        raise ValueError(f"Unsupported source unit: {from_unit}")
    if to_unit not in units_to_base:
        raise ValueError(f"Unsupported target unit: {to_unit}")
    
    base_value = distance * units_to_base[from_unit]
    
    factor = units_to_base[to_unit]
    if factor == 0:
        return 0.0
    
    result = base_value / factor
    return result

if __name__ == '__main__':
    distance = 1000
    from_unit = 'meter'
    to_unit = 'kilometer'
    result = convert_distance(distance, from_unit, to_unit)
    print(result)
    
    distance = 1
    from_unit = 'mile'
    to_unit = 'kilometer'
    result = convert_distance(distance, from_unit, to_unit)
    print(result)
    
    distance = 0
    from_unit = 'meter'
    to_unit = 'foot'
    result = convert_distance(distance, from_unit, to_unit)
    print(result)