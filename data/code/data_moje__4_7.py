def normalize_distance(value, unit):
    unit = unit.lower().strip()
    conversion_factors = {
        'meter': 1.0,
        'metre': 1.0,
        'm': 1.0,
        'kilometer': 1000.0,
        'kilometre': 1000.0,
        'km': 1000.0,
        'centimeter': 0.01,
        'centimetre': 0.01,
        'cm': 0.01,
        'millimeter': 0.001,
        'millimetre': 0.001,
        'mm': 0.001,
        'micrometer': 1e-6,
        'micrometre': 1e-6,
        'micron': 1e-6,
        'um': 1e-6,
        'mile': 1609.344,
        'nautical_mile': 1852.0,
        'nm': 1852.0,
        'yard': 0.9144,
        'yd': 0.9144,
        'foot': 0.3048,
        'feet': 0.3048,
        'ft': 0.3048,
        'inch': 0.0254,
        'in': 0.0254,
        'light_year': 9.461e15,
        'ly': 9.461e15,
        'astronomical_unit': 1.496e11,
        'au': 1.496e11,
        'parsec': 3.086e16,
        'pc': 3.086e16
    }
    if unit not in conversion_factors:
        raise ValueError(f"Unknown unit: {unit}")
    return value * conversion_factors[unit]

if __name__ == '__main__':
    samples = [
        (1000, 'km'),
        (5280, 'ft'),
        (1, 'mile'),
        (1, 'in'),
        (3, 'yards'),
        (100, 'cm')
    ]
    for val, unit in samples:
        result = normalize_distance(val, unit)
        print(f"{val} {unit} = {result} meters")