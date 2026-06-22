def normalize_to_meters(value, unit):
    unit = unit.lower().strip()
    if unit in ('m', 'meter', 'meters'):
        return value
    elif unit in ('km', 'kilometer', 'kilometers'):
        return value * 1000.0
    elif unit in ('cm', 'centimeter', 'centimeters'):
        return value * 0.01
    elif unit in ('mm', 'millimeter', 'millimeters'):
        return value * 0.001
    elif unit in ('mi', 'mile', 'miles'):
        return value * 1609.344
    elif unit in ('yd', 'yard', 'yards'):
        return value * 0.9144
    elif unit in ('ft', 'feet', 'foot'):
        return value * 0.3048
    elif unit in ('in', 'inch', 'inches'):
        return value * 0.0254
    elif unit in ('nm', 'nanometer', 'nanometers'):
        return value * 1e-9
    elif unit in ('um', 'micrometer', 'micrometers', 'µm'):
        return value * 1e-6
    else:
        raise ValueError(f"Unknown unit: {unit}")

if __name__ == '__main__':
    print(normalize_to_meters(1, 'km'))
    print(normalize_to_meters(100, 'cm'))
    print(normalize_to_meters(5, 'mi'))
    print(normalize_to_meters(12, 'in'))
    print(normalize_to_meters(1, 'm'))
    print(normalize_to_meters(1000, 'nm'))