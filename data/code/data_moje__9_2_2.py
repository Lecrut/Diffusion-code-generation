def convert_volume(volume, target_unit):
    conversion_factors = {
        'L': 1.0,
        'm3': 0.001,
        'gal': 0.264172,
        'ml': 1000.0,
        'ft3': 0.0353147,
        'cup': 4.22675,
        'tbsp': 67.628,
        'tsp': 202.884
    }
    if target_unit not in conversion_factors:
        raise ValueError(f"Unsupported unit: {target_unit}")
    return volume * conversion_factors[target_unit]

if __name__ == '__main__':
    print(convert_volume(1, 'L'))
    print(convert_volume(1, 'm3'))
    print(convert_volume(1, 'gal'))
    print(convert_volume(1000, 'ml'))
    print(convert_volume(1, 'ft3'))
    print(convert_volume(1, 'cup'))
    print(convert_volume(1, 'tbsp'))
    print(convert_volume(1, 'tsp'))