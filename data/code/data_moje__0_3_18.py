def convert_length(length_str, target_unit):
    unit_map = {
        'm': 1.0,
        'cm': 0.01,
        'mm': 0.001,
        'km': 1000.0,
        'in': 0.0254,
        'ft': 0.3048,
        'yd': 0.9144,
        'mi': 1609.344
    }

    try:
        value = float(length_str)
    except (ValueError, TypeError):
        raise ValueError("Invalid length value")

    if target_unit not in unit_map:
        raise ValueError(f"Unsupported target unit: {target_unit}")

    source_unit = None
    for unit, factor in unit_map.items():
        if length_str.lower().endswith(unit):
            try:
                numeric_part = length_str[:-len(unit)].strip()
                if numeric_part == '':
                    raise ValueError()
                value = float(numeric_part)
                source_unit = unit
                break
            except ValueError:
                continue

    if source_unit is None:
        raise ValueError("Could not determine source unit from string")

    if source_unit not in unit_map:
        raise ValueError(f"Unsupported source unit: {source_unit}")

    meters = value * unit_map[source_unit]
    result = meters / unit_map[target_unit]
    return result

if __name__ == '__main__':
    print(convert_length("10m", 'ft'))
    print(convert_length("5.5km", 'mi'))
    print(convert_length("100cm", 'in'))