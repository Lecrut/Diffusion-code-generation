def convert_volume(volume, target_unit):
    unit_conversions = {
        'L': 1.0,
        'm3': 1000.0,
        'gal': 3.78541,
        'ft3': 28.3168,
        'ml': 1000.0,
    }
    if target_unit not in unit_conversions:
        raise ValueError(f"Unknown target unit: {target_unit}")
    if target_unit == 'L':
        return volume
    else:
        return volume * unit_conversions[target_unit]
if __name__ == '__main__':
    volume_value = 5
    target_unit_1 = 'L'
    target_unit_2 = 'm3'
    target_unit_3 = 'gal'
    target_unit_4 = 'ft3'
    target_unit_5 = 'unknown'
    result1 = convert_volume(volume_value, target_unit_1)
    result2 = convert_volume(volume_value, target_unit_2)
    result3 = convert_volume(volume_value, target_unit_3)
    result4 = convert_volume(volume_value, target_unit_4)
    print(f"Volume: {volume_value} L -> {result1:.4f} L")
    print(f"Volume: {volume_value} L -> {result2:.4f} m3")
    print(f"Volume: {volume_value} L -> {result3:.4f} gal")
    print(f"Volume: {volume_value} L -> {result4:.4f} ft3")
    try:
        convert_volume(volume_value, target_unit_5)
    except ValueError as e:
        print(f"Error: {e}")