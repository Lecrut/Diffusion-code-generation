def convert_length(value, from_unit, to_unit):
    unit_to_meters = {
        'mm': 0.001,
        'cm': 0.01,
        'm': 1.0,
        'km': 1000.0,
        'in': 0.0254,
        'ft': 0.3048,
        'yd': 0.9144,
        'mi': 1609.344,
        'nmi': 1852.0,
        'um': 1e-6,
        'nm': 1e-9,
    }
    from_unit = from_unit.lower()
    to_unit = to_unit.lower()
    if from_unit not in unit_to_meters:
        raise ValueError(f"Unsupported source unit: {from_unit}")
    if to_unit not in unit_to_meters:
        raise ValueError(f"Unsupported target unit: {to_unit}")
    meters = value * unit_to_meters[from_unit]
    result = meters / unit_to_meters[to_unit]
    return result

if __name__ == '__main__':
    print(convert_length(1, 'mi', 'km'))
    print(convert_length(100, 'cm', 'in'))
    print(convert_length(5, 'ft', 'm'))
    print(convert_length(1, 'nmi', 'mi'))