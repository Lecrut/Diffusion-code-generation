def convert_distance(distance, target_unit):
    units = {
        'meter': 1.0,
        'kilometer': 1000.0,
        'centimeter': 0.01,
        'millimeter': 0.001,
        'mile': 1609.344,
        'yard': 0.9144,
        'foot': 0.3048,
        'inch': 0.0254,
        'nautical_mile': 1852.0
    }

    target_unit_lower = target_unit.lower()
    if target_unit_lower not in units:
        raise ValueError(f"Unsupported unit: {target_unit}")

    base_distance = distance * units[target_unit_lower]
    return base_distance

if __name__ == '__main__':
    print(convert_distance(1, 'meter'))
    print(convert_distance(1, 'kilometer'))
    print(convert_distance(100, 'centimeter'))
    print(convert_distance(1, 'mile'))
    print(convert_distance(50, 'foot'))
    print(convert_distance(1, 'nautical_mile'))
    try:
        convert_distance(1, 'lightyear')
    except ValueError as e:
        print(str(e))