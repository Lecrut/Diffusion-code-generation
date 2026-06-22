def convert_length(value: str, target_unit: str) -> float:
    units_to_meters = {
        'm': 1.0,
        'km': 1000.0,
        'cm': 0.01,
        'mm': 0.001,
        'ft': 0.3048,
        'in': 0.0254,
        'yd': 0.9144,
        'mi': 1609.344,
    }
    
    value_str = value.strip()
    if not value_str:
        raise ValueError("Empty value string")
    
    try:
        numeric_value = float(value_str)
    except ValueError:
        raise ValueError(f"Invalid numeric value: {value_str}")
    
    if target_unit not in units_to_meters:
        raise ValueError(f"Unknown target unit: {target_unit}")
    
    target_factor = units_to_meters[target_unit]
    
    converted_value = numeric_value * target_factor
    
    return converted_value

if __name__ == '__main__':
    result = convert_length("100 cm", "ft")
    print(result)