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
    volume_liters = 5.0
    target_unit_m3 = 'm3'
    result_m3 = convert_volume(volume_liters, target_unit_m3)
    print(f"Converted {volume_liters} L to {target_unit_m3}: {result_m3}")
    volume_gal = 10.0
    target_unit_l = 'L'
    result_l = convert_volume(volume_gal, target_unit_l)
    print(f"Converted {volume_gal} gal to {target_unit_l}: {result_l}")
    volume_m3_to_gal = 2.5
    target_unit_gal = 'gal'
    result_gal = convert_volume(volume_m3_to_gal, target_unit_gal)
    print(f"Converted {volume_m3_to_gal} m3 to {target_unit_gal}: {result_gal}")
    volume_unknown = 10.0
    target_unit_unknown = 'ft3'
    try:
        result_unknown = convert_volume(volume_unknown, target_unit_unknown)
        print(f"Converted {volume_unknown} (error test) to {target_unit_unknown}: {result_unknown}")
    except ValueError as e:
        print(f"Error caught: {e}")