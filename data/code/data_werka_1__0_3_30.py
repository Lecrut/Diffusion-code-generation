def convert_length(value_str, target_unit):
    units = {
        'm': 1.0,
        'ft': 0.3048,
        'cm': 0.01,
        'mm': 0.001,
        'in': 0.0254,
        'yd': 0.9144,
        'km': 1000.0,
        'mi': 1609.344
    }
    
    value_str = value_str.strip()
    if not value_str:
        raise ValueError("Value string cannot be empty")
        
    try:
        value = float(value_str)
    except ValueError:
        raise ValueError(f"Invalid numeric value: {value_str}")
        
    target_unit_lower = target_unit.lower()
    
    if target_unit_lower not in units:
        raise ValueError(f"Unsupported target unit: {target_unit}")
        
    meters = value * units[target_unit_lower]
    result = meters / units[target_unit_lower]
    
    return result

if __name__ == '__main__':
    print(convert_length("10 m", "ft"))
    print(convert_length("5.28 ft", "m"))
    print(convert_length("1 km", "mi"))