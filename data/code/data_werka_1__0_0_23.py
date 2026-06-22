def convert_length(value: float, unit_from: str) -> dict:
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

    if unit_from not in conversions:
        raise ValueError(f"Unsupported unit type: {unit_from}")

    meters = value * conversions[unit_from]

    result = {}
    for unit, factor in conversions.items():
        result[unit] = meters / factor

    return result

if __name__ == '__main__':
    length = 1.0
    unit_type = 'ft'
    
    converted_values = convert_length(length, unit_type)
    
    for unit, val in converted_values.items():
        print(f"{val:.6f} {unit}")