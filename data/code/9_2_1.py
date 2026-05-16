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
    else:
        return volume * unit_conversions[target_unit]
if __name__ == '__main__':
    volume_value = 5
    target_unit_1 = 'L'
    target_unit_2 = 'm3'
    target_unit_3 = 'gal'
    target_unit_4 = 'ml'
    result_1 = convert_volume(volume_value, target_unit_1)
    result_2 = convert_volume(volume_value, target_unit_2)
    result_3 = convert_volume(volume_value, target_unit_3)
    result_4 = convert_volume(volume_value, target_unit_4)
    print(f"Volume: {volume_value} L -> {result_1} L")
    print(f"Volume: {volume_value} L -> {result_2} m3")
    print(f"Volume: {volume_value} L -> {result_3} gal")
    print(f"Volume: {volume_value} L -> {result_4} ml")