def convert_length(value, from_unit, to_unit):
    units = {
        'mm': 0.001,
        'cm': 0.01,
        'm': 1.0,
        'km': 1000.0,
        'in': 0.0254,
        'ft': 0.3048,
        'yd': 0.9144,
        'mi': 1609.344
    }
    from_unit_lower = from_unit.lower()
    to_unit_lower = to_unit.lower()
    if from_unit_lower not in units:
        raise ValueError(f"Unsupported source unit: {from_unit}")
    if to_unit_lower not in units:
        raise ValueError(f"Unsupported target unit: {to_unit}")
    value_in_meters = value * units[from_unit_lower]
    result = value_in_meters / units[to_unit_lower]
    return result

if __name__ == '__main__':
    print(convert_length(1, 'mi', 'km'))
    print(convert_length(100, 'cm', 'in'))
    print(convert_length(1, 'km', 'mi'))
    print(convert_length(5000, 'mm', 'm'))
    print(convert_length(10, 'ft', 'cm'))