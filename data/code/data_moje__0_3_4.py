def convert_length(length_str: str, target_unit: str) -> float:
    units_to_meters = {
        'm': 1.0,
        'cm': 0.01,
        'mm': 0.001,
        'km': 1000.0,
        'in': 0.0254,
        'ft': 0.3048,
        'yd': 0.9144,
        'mi': 1609.344,
    }
    
    if target_unit not in units_to_meters:
        raise ValueError(f"Unsupported target unit: {target_unit}")
    
    length_str = length_str.strip().lower()
    length_value = 0.0
    source_unit = 'm'
    
    found_unit = False
    for unit, factor in units_to_meters.items():
        if length_str.endswith(unit):
            source_unit = unit
            length_value = float(length_str[:-len(unit)].strip())
            found_unit = True
            break
    
    if not found_unit:
        try:
            length_value = float(length_str)
            source_unit = 'm'
        except ValueError:
            raise ValueError(f"Invalid length string: {length_str}")
    
    if source_unit not in units_to_meters:
        raise ValueError(f"Unsupported source unit: {source_unit}")
    
    value_in_meters = length_value * units_to_meters[source_unit]
    result = value_in_meters / units_to_meters[target_unit]
    
    return result

if __name__ == '__main__':
    result = convert_length("100 cm", "m")
    print(result)