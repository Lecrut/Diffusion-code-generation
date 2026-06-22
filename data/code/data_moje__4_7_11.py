def normalize_to_meters(value, unit):
    unit = unit.lower().strip()
    factors = {
        'mm': 0.001,
        'millimeter': 0.001,
        'millimeters': 0.001,
        'cm': 0.01,
        'centimeter': 0.01,
        'centimeters': 0.01,
        'm': 1.0,
        'meter': 1.0,
        'meters': 1.0,
        'km': 1000.0,
        'kilometer': 1000.0,
        'kilometers': 1000.0,
        'in': 0.0254,
        'inch': 0.0254,
        'inches': 0.0254,
        'ft': 0.3048,
        'foot': 0.3048,
        'feet': 0.3048,
        'mi': 1609.344,
        'mile': 1609.344,
        'miles': 1609.344,
        'yd': 0.9144,
        'yard': 0.9144,
        'yards': 0.9144
    }
    if unit not in factors:
        raise ValueError(f"Unknown unit: {unit}")
    return value * factors[unit]

if __name__ == '__main__':
    results = []
    results.append(normalize_to_meters(1000, 'mm'))
    results.append(normalize_to_meters(100, 'cm'))
    results.append(normalize_to_meters(1, 'm'))
    results.append(normalize_to_meters(5, 'km'))
    results.append(normalize_to_meters(10, 'in'))
    results.append(normalize_to_meters(6, 'ft'))
    results.append(normalize_to_meters(1, 'mi'))
    results.append(normalize_to_meters(3, 'yd'))
    for r in results:
        print(r)