def normalize_distance(value, unit):
    unit = unit.lower().strip()
    units_to_meters = {
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
        'miles': 1609.344,
        'mile': 1609.344,
        'nmi': 1852.0,
        'nautical mile': 1852.0,
        'nautical miles': 1852.0
    }
    if unit not in units_to_meters:
        raise ValueError(f"Unsupported unit: {unit}")
    return value * units_to_meters[unit]

if __name__ == '__main__':
    samples = [
        (100, 'mm'),
        (50, 'cm'),
        (1, 'm'),
        (2.5, 'km'),
        (10, 'in'),
        (5, 'ft'),
        (1, 'miles'),
        (0.5, 'nautical miles')
    ]
    for value, unit in samples:
        result = normalize_distance(value, unit)
        print(f"{value} {unit} = {result} meters")