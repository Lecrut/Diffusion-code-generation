def convert_length(value_str: str, target_unit: str) -> float:
    units_to_meters = {
        'm': 1.0,
        'ft': 0.3048,
        'in': 0.0254,
        'cm': 0.01,
        'mm': 0.001,
        'km': 1000.0,
        'mi': 1609.344,
        'yd': 0.9144,
    }

    if target_unit not in units_to_meters:
        raise ValueError(f"Unsupported target unit: {target_unit}")

    value_str = value_str.strip()
    try:
        parts = value_str.split()
        if len(parts) != 2:
            raise ValueError("Input must be in format '<value> <unit>'")
        
        value = float(parts[0])
        source_unit = parts[1]
        
        if source_unit not in units_to_meters:
            raise ValueError(f"Unsupported source unit: {source_unit}")
            
    except ValueError as e:
        raise ValueError(f"Invalid input format or value: {e}")

    meters = value * units_to_meters[source_unit]
    converted_value = meters / units_to_meters[target_unit]
    
    return converted_value

if __name__ == '__main__':
    result = convert_length("10 m", 'ft')
    print(result)