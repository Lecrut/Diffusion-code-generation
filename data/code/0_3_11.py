def convert_length(length_str: str, target_unit: str) -> float:
    conversions = {
        'm': 1.0,
        'cm': 0.01,
        'mm': 0.001,
        'km': 1000.0,
        'in': 0.0254,
        'ft': 0.3048,
        'yd': 0.9144,
        'mi': 1609.344,
    }
    
    length_str = length_str.strip()
    
    parsed_value = 0.0
    parsed_unit = None
    
    if length_str.endswith('mm'):
        parsed_value = float(length_str[:-2])
        parsed_unit = 'mm'
    elif length_str.endswith('cm'):
        parsed_value = float(length_str[:-2])
        parsed_unit = 'cm'
    elif length_str.endswith('km'):
        parsed_value = float(length_str[:-2])
        parsed_unit = 'km'
    elif length_str.endswith('in'):
        parsed_value = float(length_str[:-2])
        parsed_unit = 'in'
    elif length_str.endswith('ft'):
        parsed_value = float(length_str[:-2])
        parsed_unit = 'ft'
    elif length_str.endswith('yd'):
        parsed_value = float(length_str[:-2])
        parsed_unit = 'yd'
    elif length_str.endswith('mi'):
        parsed_value = float(length_str[:-2])
        parsed_unit = 'mi'
    elif length_str.endswith('m'):
        parsed_value = float(length_str[:-1])
        parsed_unit = 'm'
    else:
        raise ValueError(f"Unknown unit in length string: {length_str}")
        
    if parsed_unit not in conversions or target_unit not in conversions:
        raise ValueError(f"Unsupported unit conversion. Available: {list(conversions.keys())}")
        
    length_in_meters = parsed_value * conversions[parsed_unit]
    result_in_target = length_in_meters / conversions[target_unit]
    
    return result_in_target

if __name__ == '__main__':
    print(convert_length("100 cm", "m"))
    print(convert_length("5.5 ft", "m"))
    print(convert_length("1 km", "mi"))
    print(convert_length("12 in", "cm"))
    print(convert_length("3 yd", "ft"))