VOLUME_FACTORS = {
    'L': 1.0,
    'm3': 1000.0,
    'gal': 3.78541,
    'ml': 0.001,
    'oz': 0.0295735,
    'ft3': 28.3168,
    'qt': 0.946353,
    'pt': 0.473176,
    'cup': 0.236588
}

def convert_volume(value, target_unit):
    source_unit = 'L'
    if target_unit not in VOLUME_FACTORS:
        raise ValueError(f"Unsupported target unit: {target_unit}")
    base_value = value * VOLUME_FACTORS.get(source_unit, 1.0)
    return base_value / VOLUME_FACTORS[target_unit]

if __name__ == '__main__':
    test_value = 50
    target = 'gal'
    result = convert_volume(test_value, target)
    print(result)
    target_m3 = 'm3'
    result_m3 = convert_volume(5000, target_m3)
    print(result_m3)