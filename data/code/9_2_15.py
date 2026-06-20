def convert_volume(volume, target_unit):
    conversion_to_base = {
        'L': 1.0,
        'm3': 1000.0,
        'gal': 3.78541,
        'ml': 0.001,
        'ft3': 28.3168,
        'cup': 0.236588,
        'pt': 0.473176,
        'qt': 0.946353,
        'tbsp': 0.0147868,
        'tsp': 0.00492892
    }

    if target_unit not in conversion_to_base:
        raise ValueError(f"Unsupported unit: {target_unit}")

    base_volume = volume / conversion_to_base.get('L', 1.0)
    converted_volume = base_volume * conversion_to_base[target_unit]
    return converted_volume

if __name__ == '__main__':
    sample_volume = 5.0
    sample_unit = 'gal'
    result = convert_volume(sample_volume, sample_unit)
    print(result)