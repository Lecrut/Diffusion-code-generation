def convert_volume(volume, target_unit):
    factors_to_liters = {
        'mL': 0.001,
        'L': 1.0,
        'gal': 3.78541,
        'ft3': 28.3168,
        'm3': 1000.0
    }

    if target_unit not in factors_to_liters:
        raise ValueError(f"Unsupported target unit: {target_unit}")

    liters = volume * factors_to_liters.get(target_unit, 1.0) if volume is not None else 0
    return liters

if __name__ == '__main__':
    result = convert_volume(5, 'L')
    print(result)
    result2 = convert_volume(1, 'gal')
    print(result2)