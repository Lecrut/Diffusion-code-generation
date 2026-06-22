import re

def convert_length(value_str, target_unit):
    unit_map = {
        'm': 1.0,
        'km': 1000.0,
        'cm': 0.01,
        'mm': 0.001,
        'ft': 0.3048,
        'in': 0.0254,
        'yd': 0.9144,
        'mi': 1609.344,
    }
    
    value_str = value_str.strip()
    if not value_str:
        raise ValueError("Input string is empty")
    
    pattern = r'^([+-]?\d*\.?\d+)\s*([a-zA-Z]+)$'
    match = re.match(pattern, value_str)
    
    if not match:
        raise ValueError("Invalid format. Expected format like '10.5 m'")
    
    value = float(match.group(1))
    source_unit = match.group(2).lower()
    
    if source_unit not in unit_map:
        raise ValueError(f"Unsupported source unit: {source_unit}")
    
    target_unit_lower = target_unit.strip().lower()
    if target_unit_lower not in unit_map:
        raise ValueError(f"Unsupported target unit: {target_unit_lower}")
    
    value_in_meters = value * unit_map[source_unit]
    result = value_in_meters / unit_map[target_unit_lower]
    
    return result

if __name__ == '__main__':
    sample_input = "10.5 ft"
    target = "m"
    converted_value = convert_length(sample_input, target)
    print(converted_value)
    
    sample_input_2 = "100 cm"
    target_2 = "in"
    converted_value_2 = convert_length(sample_input_2, target_2)
    print(converted_value_2)