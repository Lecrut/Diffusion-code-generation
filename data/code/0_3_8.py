def convert_length(value_str, target_unit):
    conversion_factors = {
        'm': 1.0,
        'ft': 0.3048,
        'in': 0.0254,
        'cm': 0.01,
        'km': 1000.0,
        'mi': 1609.34,
        'yd': 0.9144
    }
    
    units_in_dict = {
        'm': 'm',
        'ft': 'ft',
        'in': 'in',
        'cm': 'cm',
        'km': 'km',
        'mi': 'mi',
        'yd': 'yd'
    }
    
    try:
        numeric_value = float(value_str)
    except ValueError:
        raise ValueError("Invalid numeric value provided")
    
    if target_unit not in conversion_factors:
        raise ValueError(f"Unsupported target unit: {target_unit}")
    
    value_in_meters = numeric_value * conversion_factors[target_unit]
    
    source_unit = None
    for unit_key, unit_name in units_in_dict.items():
        if unit_key in value_str.lower() and unit_key != target_unit:
            source_unit = unit_key
            break
    
    if source_unit is None:
        source_unit = 'm'
    
    if source_unit not in conversion_factors:
        raise ValueError(f"Could not determine source unit from: {value_str}")
    
    value_in_target = value_in_meters / conversion_factors[source_unit]
    
    return round(value_in_target, 6)

if __name__ == '__main__':
    result1 = convert_length("10 ft", "m")
    print(result1)
    result2 = convert_length("5.5 m", "ft")
    print(result2)
    result3 = convert_length("100 cm", "in")
    print(result3)