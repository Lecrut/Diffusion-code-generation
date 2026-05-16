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
        return "Error: Unknown target unit"
    if volume == 0:
        return 0.0
    unit_to_liter = {
        'L': 1.0,
        'm3': 1000.0,
        'gal': 3.78541,
        'Liters': 1.0,
        'm3': 1000.0,
        'gallons': 3.78541
    }
    if target_unit not in unit_to_liter:
        return "Error: Unknown target unit"
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
    print(f"Convert 10 Liters to m3: {convert_volume(10, 'm3')}")
    print(f"Convert 5000 m3 to L: {convert_volume(5000, 'L')}")
    print(f"Convert 100 gallons to Liters: {convert_volume(100, 'Liters')}")
    print(f"Convert 10000 L to gal: {convert_volume(10000, 'gal')}")
    print(f"Convert 0 to m3: {convert_volume(0, 'm3')}")
    print(f"Convert 10 L to L: {convert_volume(10, 'L')}")
    print(f"Convert 10 L to oz (Unknown): {convert_volume(10, 'oz')}")