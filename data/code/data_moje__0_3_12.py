def convert_length(length_str, target_unit):
    units = {
        'm': 1.0,
        'ft': 3.28084,
        'in': 39.3701,
        'cm': 100.0,
        'mm': 1000.0,
        'km': 0.001,
        'mi': 0.000621371,
        'yd': 1.09361
    }
    if target_unit not in units:
        raise ValueError(f"Unsupported unit: {target_unit}")
    if ' ' in length_str:
        parts = length_str.split()
        if len(parts) != 2:
            raise ValueError("Invalid length format. Expected 'value unit'")
        value = float(parts[0])
        source_unit = parts[1]
    else:
        value = float(length_str)
        source_unit = 'm'
    if source_unit not in units:
        raise ValueError(f"Unsupported source unit: {source_unit}")
    value_in_meters = value / units[source_unit]
    result = value_in_meters * units[target_unit]
    return result

if __name__ == '__main__':
    test_cases = [
        ("1 m", "ft"),
        ("100 cm", "in"),
        ("5 ft", "m"),
        ("2.5 km", "mi"),
        ("12 in", "cm")
    ]
    for length, unit in test_cases:
        result = convert_length(length, unit)
        print(f"{length} to {unit} is {result}")