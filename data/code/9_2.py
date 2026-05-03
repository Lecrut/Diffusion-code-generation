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
        volume_in_liters = volume
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
    volume_value = 500
    target_unit_1 = 'm3'
    target_unit_2 = 'gal'
    target_unit_3 = 'L'
    print(f"Converting {volume_value} (assumed Liters) to {target_unit_1}: {convert_volume(volume_value, target_unit_1)}")
    print(f"Converting {volume_value} (assumed Liters) to {target_unit_2}: {convert_volume(volume_value, target_unit_2)}")
    print(f"Converting {volume_value} (assumed Liters) to {target_unit_3}: {convert_volume(volume_value, target_unit_3)}")
    volume_value_2 = 1000
    target_unit_4 = 'Liters'
    print(f"Converting {volume_value_2} (assumed Liters) to {target_unit_4}: {convert_volume(volume_value_2, target_unit_4)}")
    volume_value_3 = 10
    target_unit_5 = 'unknown'
    try:
        print(f"Attempting conversion to {target_unit_5}: {convert_volume(volume_value_3, target_unit_5)}")
    except ValueError as e:
        print(f"Error caught: {e}")