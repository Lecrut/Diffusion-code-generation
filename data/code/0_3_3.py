def convert_length(length_str, target_unit):
    unit_factors = {
        'mm': 0.001,
        'cm': 0.01,
        'm': 1.0,
        'km': 1000.0,
        'in': 0.0254,
        'ft': 0.3048,
        'yd': 0.9144,
        'mi': 1609.344
    }

    parts = length_str.strip().split()
    if len(parts) != 2:
        raise ValueError("Input must be in format '<number> <unit>'")

    try:
        value = float(parts[0])
    except ValueError:
        raise ValueError("Numeric part is not a valid number")

    source_unit = parts[1].lower()
    target_unit = target_unit.lower()

    if source_unit not in unit_factors:
        raise ValueError(f"Unknown source unit: {source_unit}")
    if target_unit not in unit_factors:
        raise ValueError(f"Unknown target unit: {target_unit}")

    meters = value * unit_factors[source_unit]
    result = meters / unit_factors[target_unit]
    return result

if __name__ == '__main__':
    print(convert_length('1 m', 'ft'))
    print(convert_length('5 km', 'mi'))
    print(convert_length('100 cm', 'in'))