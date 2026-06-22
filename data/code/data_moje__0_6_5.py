def convert_length(value, from_unit, to_unit):
    units_to_meters = {
        'm': 1.0,
        'km': 1000.0,
        'cm': 0.01,
        'mm': 0.001,
        'mi': 1609.344,
        'yd': 0.9144,
        'ft': 0.3048,
        'in': 0.0254,
        'nmi': 1852.0
    }

    from_unit_lower = from_unit.lower()
    to_unit_lower = to_unit.lower()

    if from_unit_lower not in units_to_meters:
        raise ValueError(f"Unsupported source unit: {from_unit}")
    if to_unit_lower not in units_to_meters:
        raise ValueError(f"Unsupported target unit: {to_unit}")

    value_in_meters = value * units_to_meters[from_unit_lower]
    result = value_in_meters / units_to_meters[to_unit_lower]
    return result

if __name__ == '__main__':
    print(convert_length(1, 'km', 'mi'))
    print(convert_length(5, 'ft', 'cm'))
    print(convert_length(100, 'm', 'ft'))
    print(convert_length(1, 'mi', 'km'))
    print(convert_length(2.5, 'in', 'mm'))