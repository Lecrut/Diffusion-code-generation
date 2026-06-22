def convert_length(value_str, target_unit):
    conversions = {
        'm': 1.0,
        'km': 1000.0,
        'cm': 0.01,
        'mm': 0.001,
        'ft': 0.3048,
        'in': 0.0254,
        'yd': 0.9144,
        'mi': 1609.344,
    }

    value_str = value_str.strip().lower()
    if target_unit not in conversions:
        raise ValueError(f"Unsupported target unit: {target_unit}")

    known_units = [k for k in conversions.keys() if len(k) < len(value_str) and value_str.endswith(k)]
    if not known_units:
        raise ValueError(f"Could not determine source unit from '{value_str}'")

    source_unit = sorted(known_units, key=len, reverse=True)[0]
    numeric_part = value_str[:-len(source_unit)]
    if not numeric_part:
        raise ValueError(f"Invalid value format for '{source_unit}'")

    value = float(numeric_part)
    base_value = value * conversions[source_unit]
    result = base_value / conversions[target_unit]

    return result

if __name__ == '__main__':
    print(convert_length('10m', 'ft'))
    print(convert_length('5.5km', 'mi'))
    print(convert_length('12in', 'cm'))