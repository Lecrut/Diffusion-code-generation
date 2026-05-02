def convert_volume(volume, target_unit):
    conversion_factors = {
        'L': 1.0,
        'm3': 1000.0,
        'gal': 3.78541,
        'L_to_m3': 0.001,
        'm3_to_L': 1000.0,
        'gal_to_L': 3.78541,
    }
    if target_unit == 'L':
        if volume == 0:
            return 0.0
        if 'L_to_m3' in conversion_factors:
            return volume * conversion_factors['L_to_m3']
        elif 'm3_to_L' in conversion_factors:
            return volume * conversion_factors['m3_to_L']
        elif 'gal_to_L' in conversion_factors:
            return volume * conversion_factors['gal_to_L']
        else:
            return volume
    elif target_unit == 'm3':
        if 'L_to_m3' in conversion_factors:
            return volume * conversion_factors['L_to_m3']
        elif 'm3_to_L' in conversion_factors:
            return volume / conversion_factors['m3_to_L']
        elif 'gal_to_L' in conversion_factors:
            return volume * conversion_factors['gal_to_L'] * conversion_factors['L_to_m3']
        else:
            return volume
    elif target_unit == 'gal':
        if 'gal_to_L' in conversion_factors:
            return volume / conversion_factors['gal_to_L']
        elif 'm3_to_L' in conversion_factors:
            return (volume / conversion_factors['m3_to_L']) / conversion_factors['gal_to_L']
        elif 'L_to_m3' in conversion_factors:
            return (volume * conversion_factors['L_to_m3']) / conversion_factors['gal_to_L']
        else:
            return volume
    else:
        return volume
if __name__ == '__main__':
    volume_liters = 10.0
    target_unit_m3 = 'm3'
    result_m3 = convert_volume(volume_liters, target_unit_m3)
    print(f"Converting {volume_liters} L to {target_unit_m3}: {result_m3}")
    volume_m3 = 5.0
    target_unit_gal = 'gal'
    result_gal = convert_volume(volume_m3, target_unit_gal)
    print(f"Converting {volume_m3} m3 to {target_unit_gal}: {result_gal}")
    volume_gal = 10.0
    target_unit_l = 'L'
    result_l = convert_volume(volume_gal, target_unit_l)
    print(f"Converting {volume_gal} gal to {target_unit_l}: {result_l}")