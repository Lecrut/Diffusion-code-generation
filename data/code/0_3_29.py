def convert_length(value_str, target_unit):
    units_to_meters = {
        'm': 1.0,
        'ft': 0.3048,
        'in': 0.0254,
        'cm': 0.01,
        'mm': 0.001,
        'km': 1000.0,
        'yd': 0.9144,
        'mi': 1609.344
    }

    value_str = value_str.strip()
    
    if not any(char.isdigit() or char == '.' for char in value_str):
        raise ValueError("Invalid numeric format")

    try:
        magnitude = float(value_str)
    except ValueError:
        raise ValueError("Could not parse number from string")

    unit_char = target_unit.strip().lower()
    
    if unit_char not in units_to_meters:
        raise ValueError(f"Unsupported target unit: {target_unit}")

    meters = magnitude * units_to_meters[unit_char]
    
    result_in_target = meters / units_to_meters[target_unit]
    
    return result_in_target

if __name__ == '__main__':
    sample_input = "100 cm"
    target = 'in'
    result = convert_length(sample_input, target)
    print(result)