def normalize_to_meters(value, unit):
    unit = unit.lower().strip()
    conversion_factors = {
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
        'yards': 0.9144,
        'nmi': 1852.0,
        'nautical_mile': 1852.0,
        'nautical_miles': 1852.0,
    }
    
    if unit in conversion_factors:
        return value * conversion_factors[unit]
    else:
        raise ValueError(f"Unsupported unit: {unit}")

if __name__ == '__main__':
    samples = [
        (1000, 'mm'),
        (1.5, 'km'),
        (1, 'mi'),
        (60, 'in'),
        (5, 'yd')
    ]
    
    for value, unit in samples:
        result = normalize_to_meters(value, unit)
        print(f"{value} {unit} = {result} meters")