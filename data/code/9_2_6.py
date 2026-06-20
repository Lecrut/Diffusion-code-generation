VOLUME_TO_LITERS = {
    'L': 1.0,
    'l': 1.0,
    'm3': 1000.0,
    'gal': 3.78541,
    'ml': 0.001,
    'pt': 0.473176,
    'qt': 0.946353,
    'fl_oz': 0.0295735
}

def convert_volume(value, target_unit):
    target_factor = VOLUME_TO_LITERS.get(target_unit)
    if target_factor is None:
        raise ValueError(f"Unsupported target unit: {target_unit}")
    return value / target_factor

if __name__ == '__main__':
    sample_value = 100.0
    sample_unit = 'gal'
    result = convert_volume(sample_value, sample_unit)
    print(result)