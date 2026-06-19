def convert_length(value_str: str, target_unit: str) -> float:
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

    if target_unit not in units_to_meters:
        raise ValueError(f"Unsupported target unit: {target_unit}")

    value_str = value_str.strip()
    try:
        value = float(value_str)
    except ValueError:
        raise ValueError(f"Invalid numeric string: {value_str}")

    if value < 0:
        raise ValueError("Length cannot be negative")

    meters = value * units_to_meters[target_unit]
    return meters

if __name__ == '__main__':
    result = convert_length('10 ft', 'm')
    print(result)