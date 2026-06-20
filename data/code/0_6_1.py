def convert_length(value, from_unit, to_unit):
    units_to_meters = {
        'm': 1.0,
        'mm': 0.001,
        'cm': 0.01,
        'km': 1000.0,
        'in': 0.0254,
        'ft': 0.3048,
        'yd': 0.9144,
        'mi': 1609.344,
        'μm': 1e-6,
        'nm': 1e-9,
    }

    from_unit_lower = from_unit.lower()
    to_unit_lower = to_unit.lower()

    if from_unit_lower not in units_to_meters:
        raise ValueError(f"Unsupported source unit: {from_unit}")
    if to_unit_lower not in units_to_meters:
        raise ValueError(f"Unsupported target unit: {to_unit}")

    meters = value * units_to_meters[from_unit_lower]
    result = meters / units_to_meters[to_unit_lower]
    return result

if __name__ == '__main__':
    print(convert_length(100, 'cm', 'in'))
    print(convert_length(1, 'mi', 'km'))
    print(convert_length(50, 'ft', 'm'))
    print(convert_length(1000, 'mm', 'm'))
    print(convert_length(1, 'km', 'mi'))