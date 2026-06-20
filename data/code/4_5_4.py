def convert_distance(value, from_unit, to_unit):
    if not isinstance(value, (int, float)):
        raise TypeError("Value must be a number")
    if value < 0:
        raise ValueError("Distance cannot be negative")
    unit_map = {
        'meter': 1.0,
        'kilometer': 1000.0,
        'mile': 1609.344,
        'yard': 0.9144,
        'foot': 0.3048,
        'inch': 0.0254,
        'centimeter': 0.01,
        'millimeter': 0.001
    }
    from_unit_lower = from_unit.lower()
    to_unit_lower = to_unit.lower()
    if from_unit_lower not in unit_map:
        raise ValueError(f"Unsupported source unit: {from_unit}")
    if to_unit_lower not in unit_map:
        raise ValueError(f"Unsupported target unit: {to_unit}")
    value_in_meters = value * unit_map[from_unit_lower]
    result = value_in_meters / unit_map[to_unit_lower]
    return result

if __name__ == '__main__':
    sample_value = 5
    sample_from = 'mile'
    sample_to = 'kilometer'
    result = convert_distance(sample_value, sample_from, sample_to)
    print(result)