def convert_length(value_str, target_unit):
    units = {
        'm': 1.0,
        'ft': 3.28084,
        'in': 39.3701,
        'km': 0.001,
        'mi': 0.000621371,
        'cm': 100.0,
        'mm': 1000.0,
        'yd': 1.09361,
        'nm': 1000000000.0,
    }
    
    parts = value_str.split()
    if len(parts) != 2:
        raise ValueError("Input must be in the format 'number unit' (e.g., '5 m')")
    
    try:
        number = float(parts[0])
    except ValueError:
        raise ValueError(f"First part '{parts[0]}' is not a valid number")
    
    source_unit = parts[1].strip().lower()
    
    if source_unit not in units:
        raise ValueError(f"Unsupported source unit: {source_unit}")
    if target_unit not in units:
        raise ValueError(f"Unsupported target unit: {target_unit}")
    
    value_in_meters = number / units[source_unit]
    converted_value = value_in_meters * units[target_unit]
    
    return converted_value

if __name__ == '__main__':
    sample_input = "10 ft"
    target = "m"
    result = convert_length(sample_input, target)
    print(result)
    sample_input_2 = "1 m"
    target_2 = "in"
    result_2 = convert_length(sample_input_2, target_2)
    print(result_2)
    sample_input_3 = "5 km"
    target_3 = "mi"
    result_3 = convert_length(sample_input_3, target_3)
    print(result_3)