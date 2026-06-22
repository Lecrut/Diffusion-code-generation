def normalize_to_meters(value, unit):
    unit = unit.lower().strip()
    if unit == 'meter' or unit == 'm':
        return value
    elif unit == 'kilometer' or unit == 'km':
        return value * 1000.0
    elif unit == 'centimeter' or unit == 'cm':
        return value * 0.01
    elif unit == 'millimeter' or unit == 'mm':
        return value * 0.001
    elif unit == 'micrometer' or unit == 'um' or unit == 'micrometre':
        return value * 1e-6
    elif unit == 'nanometer' or unit == 'nm':
        return value * 1e-9
    elif unit == 'mile':
        return value * 1609.344
    elif unit == 'yard' or unit == 'yd':
        return value * 0.9144
    elif unit == 'foot' or unit == 'ft' or unit == 'feet':
        return value * 0.3048
    elif unit == 'inch' or unit == 'in':
        return value * 0.0254
    elif unit == 'nautical_mile' or unit == 'nmile':
        return value * 1852.0
    else:
        raise ValueError(f"Unsupported unit: {unit}")

if __name__ == '__main__':
    samples = [
        (1000, 'km'),
        (50000, 'cm'),
        (10, 'mile'),
        (5, 'foot'),
        (200, 'nautical_mile'),
        (1, 'meter'),
        (75, 'inch')
    ]
    for value, unit in samples:
        result = normalize_to_meters(value, unit)
        print(f"{value} {unit} = {result} meters")