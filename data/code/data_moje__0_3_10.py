def convert_length(length_str, target_unit):
    unit_map = {
        'm': 1.0,
        'km': 1000.0,
        'cm': 0.01,
        'mm': 0.001,
        'in': 0.0254,
        'ft': 0.3048,
        'yd': 0.9144,
        'mi': 1609.344
    }

    parts = length_str.strip().split()
    if len(parts) != 2:
        raise ValueError("Input string must contain a number and a unit separated by space.")

    try:
        value = float(parts[0])
    except ValueError:
        raise ValueError("The numeric part of the input string is not a valid number.")

    source_unit = parts[1].lower()
    target_unit = target_unit.lower()

    if source_unit not in unit_map:
        raise ValueError(f"Unsupported source unit: {source_unit}")
    if target_unit not in unit_map:
        raise ValueError(f"Unsupported target unit: {target_unit}")

    meters = value * unit_map[source_unit]
    result = meters / unit_map[target_unit]

    return result

if __name__ == '__main__':
    sample_input = "100 m"
    sample_target = 'ft'
    result = convert_length(sample_input, sample_target)
    print(result)