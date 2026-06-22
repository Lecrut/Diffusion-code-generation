def convert_length(value_str, target_unit):
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

    value_str = value_str.strip().lower()
    
    if not any(unit in value_str for unit in units_to_meters.keys()):
        raise ValueError("Input string does not contain a recognized length unit.")

    parsed_value = None
    parsed_unit = None
    
    for unit, factor in units_to_meters.items():
        if value_str.endswith(unit):
            try:
                parsed_value = float(value_str[:-len(unit)])
                parsed_unit = unit
                break
            except ValueError:
                continue
    
    if parsed_value is None or parsed_unit is None:
        raise ValueError("Could not parse the length value and unit from the string.")

    if target_unit not in units_to_meters:
        raise ValueError(f"Target unit '{target_unit}' is not supported.")

    value_in_meters = parsed_value * units_to_meters[parsed_unit]
    converted_value = value_in_meters / units_to_meters[target_unit]
    
    return converted_value

if __name__ == '__main__':
    result = convert_length("10ft", 'm')
    print(result)