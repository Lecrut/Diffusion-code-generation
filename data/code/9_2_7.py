def convert_volume(volume, target_unit):
    unit_conversions = {
        'L': 1.0,
        'm3': 1000.0,
        'gal': 3.78541,
        'qt': 0.946353,
        'ml': 1000.0,
    }
    if target_unit not in unit_conversions:
        raise ValueError(f"Unknown target unit: {target_unit}")
    if target_unit == 'L':
        return volume
    unit_to_liters = {
        'L': 1.0,
        'm3': 1000.0,
        'gal': 3.78541,
        'qt': 0.946353,
        'ml': 1.0 / 1000.0,
    }
    if target_unit not in unit_to_liters:
        raise ValueError(f"Unknown target unit: {target_unit}")
    if target_unit == 'L':
        return volume
    volume_in_liters = volume * unit_to_liters.get(target_unit, 1.0)
    if target_unit == 'L':
        return volume
    volume_in_liters = volume * unit_to_liters[target_unit]
    inverse_factor = 1.0 / unit_to_liters[target_unit]
    result = volume_in_liters * inverse_factor
    return result
if __name__ == '__main__':
    volume_in = 10
    target_unit_1 = 'L'
    target_unit_2 = 'm3'
    target_unit_3 = 'gal'
    target_unit_4 = 'ml'
    print(f"Converting {volume_in} from unknown base to {target_unit_1}: {convert_volume(volume_in, target_unit_1)}")
    print(f"Converting {volume_in} from unknown base to {target_unit_2}: {convert_volume(volume_in, target_unit_2)}")
    print(f"Converting {volume_in} from unknown base to {target_unit_3}: {convert_volume(volume_in, target_unit_3)}")
    print(f"Converting {volume_in} from unknown base to {target_unit_4}: {convert_volume(volume_in, target_unit_4)}")
    volume_in_2 = 500
    target_unit_5 = 'm3'
    print(f"Converting {volume_in_2} from unknown base to {target_unit_5}: {convert_volume(volume_in_2, target_unit_5)}")
    try:
        convert_volume(10, 'fl')
    except ValueError as e:
        print(f"Error caught: {e}")