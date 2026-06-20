UNIT_FACTORS = {
    'meters': 1.0,
    'kilometers': 1000.0,
    'centimeters': 0.01,
    'millimeters': 0.001,
    'inches': 0.0254,
    'feet': 0.3048,
    'yards': 0.9144,
    'miles': 1609.344,
}

VALID_UNITS = set(UNIT_FACTORS.keys())

def convert_length(value, from_unit, to_unit):
    from_unit = from_unit.lower()
    to_unit = to_unit.lower()
    if from_unit not in VALID_UNITS or to_unit not in VALID_UNITS:
        raise ValueError("Invalid unit. Must be one of: {}".format(', '.join(sorted(VALID_UNITS))))
    if not isinstance(value, (int, float)):
        raise TypeError("Value must be a number")
    meters = value * UNIT_FACTORS[from_unit]
    result = meters / UNIT_FACTORS[to_unit]
    return result

if __name__ == '__main__':
    sample_values = [
        (1.0, 'meters', 'kilometers'),
        (1.0, 'kilometers', 'meters'),
        (1.0, 'meters', 'centimeters'),
        (1.0, 'meters', 'millimeters'),
        (1.0, 'meters', 'inches'),
        (1.0, 'meters', 'feet'),
        (1.0, 'meters', 'yards'),
        (1.0, 'meters', 'miles'),
        (1.0, 'miles', 'kilometers'),
        (6.0, 'feet', 'meters'),
    ]
    for value, from_u, to_u in sample_values:
        result = convert_length(value, from_u, to_u)
        print("{:.6f} {} = {:.6f} {}".format(value, from_u, result, to_u))