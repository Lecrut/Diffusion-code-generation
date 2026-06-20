def convert_length(value, from_unit, to_unit):
    units = {
        'nanometer': 1e-9,
        'micrometer': 1e-6,
        'millimeter': 1e-3,
        'centimeter': 1e-2,
        'meter': 1.0,
        'kilometer': 1000.0,
        'inch': 0.0254,
        'foot': 0.3048,
        'yard': 0.9144,
        'mile': 1609.344,
    }
    from_unit = from_unit.lower().replace(' ', '_')
    to_unit = to_unit.lower().replace(' ', '_')
    if from_unit not in units:
        raise ValueError(f"Unsupported source unit: {from_unit}")
    if to_unit not in units:
        raise ValueError(f"Unsupported target unit: {to_unit}")
    base_value = value * units[from_unit]
    return base_value / units[to_unit]

if __name__ == '__main__':
    print(convert_length(1, 'meter', 'centimeter'))
    print(convert_length(1, 'mile', 'kilometer'))
    print(convert_length(12, 'inch', 'foot'))
    print(convert_length(1000, 'millimeter', 'meter'))