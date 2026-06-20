def convert_volume(value, target_unit):
    conversion_to_base = {
        'L': 1.0,
        'm3': 1000.0,
        'gal': 3.78541,
        'ml': 0.001,
        'qt': 0.946353,
        'pt': 0.473176,
        'cup': 0.236588,
        'floz': 0.0295735,
        'tbsp': 0.0147868,
        'tsp': 0.00492892
    }

    normalized_target = target_unit.upper()

    if normalized_target not in conversion_to_base:
        raise ValueError(f"Unsupported unit: {target_unit}")

    base_value = value
    converted_value = base_value / conversion_to_base[normalized_target]

    return converted_value

if __name__ == '__main__':
    sample_value = 1
    target = 'gal'
    result = convert_volume(sample_value, target)
    print(result)

    sample_value2 = 1
    target2 = 'm3'
    result2 = convert_volume(sample_value2, target2)
    print(result2)

    sample_value3 = 5
    target3 = 'L'
    result3 = convert_volume(sample_value3, target3)
    print(result3)