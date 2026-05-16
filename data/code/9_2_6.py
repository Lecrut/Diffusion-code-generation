def convert_volume(volume, target_unit):
    conversion_factors = {
        'L': 1.0,
        'm3': 1000.0,
        'gal': 3.78541,
        'Liters': 1.0,
        'm3': 1.0,
        'gallons': 1.0
    }
    if target_unit not in conversion_factors:
        raise ValueError(f"Unknown target unit: {target_unit}")
    if volume == 0:
        return 0.0
    volume_in_liters = 0.0
    if target_unit in ['L', 'Liters']:
        volume_in_liters = volume
    elif target_unit in ['m3', 'm3']:
        volume_in_liters = volume * 1000.0
    elif target_unit in ['gal', 'gallons']:
        volume_in_liters = volume * 3.78541
    else:
        volume_in_liters = volume
    if target_unit == 'L':
        return volume_in_liters
    elif target_unit == 'm3':
        return volume_in_liters / 1000.0
    elif target_unit == 'gal':
        return volume_in_liters / 3.78541
    else:
        return volume_in_liters
if __name__ == '__main__':
    volume_liters = 10.0
    target1 = 'L'
    result1 = convert_volume(volume_liters, target1)
    print(f"Input: {volume_liters} L, Target: {target1}, Result: {result1}")
    volume_m3 = 5.0
    target2 = 'm3'
    result2 = convert_volume(volume_m3, target2)
    print(f"Input: {volume_m3} m3, Target: {target2}, Result: {result2}")
    volume_gal = 10.0
    target3 = 'gal'
    result3 = convert_volume(volume_gal, target3)
    print(f"Input: {volume_gal} gal, Target: {target3}, Result: {result3}")
    volume_unknown = 20.0
    target4 = 'unknown_unit'
    try:
        result4 = convert_volume(volume_unknown, target4)
        print(f"Input: {volume_unknown} (assumed L), Target: {target4}, Result: {result4}")
    except ValueError as e:
        print(f"Error: {e}")