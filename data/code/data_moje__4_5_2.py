def convert_distance(value, from_unit, to_unit):
    units = {
        'm': 1.0,
        'km': 1000.0,
        'cm': 0.01,
        'mm': 0.001,
        'mi': 1609.344,
        'yd': 0.9144,
        'ft': 0.3048,
        'in': 0.0254
    }
    from_unit_lower = from_unit.lower()
    to_unit_lower = to_unit.lower()
    if from_unit_lower not in units:
        raise ValueError(f"Unsupported source unit: {from_unit}")
    if to_unit_lower not in units:
        raise ValueError(f"Unsupported target unit: {to_unit}")
    if value < 0:
        raise ValueError("Distance cannot be negative")
    meters = value * units[from_unit_lower]
    result = meters / units[to_unit_lower]
    return result

if __name__ == '__main__':
    print(convert_distance(1, 'km', 'm'))
    print(convert_distance(5, 'mi', 'km'))
    print(convert_distance(100, 'cm', 'in'))