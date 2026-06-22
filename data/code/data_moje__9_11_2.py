def convert_volume(volume, source_unit, target_unit='liters'):
    conversion_rates = {
        'liters': 1.0,
        'milliliters': 1000.0,
        'gallons': 0.264172,
        'quarts': 1.05669,
        'pints': 2.11338,
        'cups': 4.22675,
        'fluid_ounces': 33.814,
        'tablespoons': 67.628,
        'teaspoons': 202.884,
        'cubic_meters': 0.001,
        'cubic_feet': 0.0353147,
        'cubic_inches': 61.0237
    }
    
    source_unit = source_unit.lower().strip()
    target_unit = target_unit.lower().strip()
    
    if source_unit not in conversion_rates:
        raise ValueError(f"Invalid source unit: {source_unit}")
    if target_unit not in conversion_rates:
        raise ValueError(f"Invalid target unit: {target_unit}")
    
    if not isinstance(volume, (int, float)):
        raise TypeError("Volume must be a number")
    
    if volume < 0:
        raise ValueError("Volume cannot be negative")
    
    volume_in_liters = volume / conversion_rates[source_unit]
    result = volume_in_liters * conversion_rates[target_unit]
    
    return result

if __name__ == '__main__':
    print(convert_volume(1, 'liters'))
    print(convert_volume(1, 'gallons', 'liters'))
    print(convert_volume(500, 'milliliters', 'cups'))
    print(convert_volume(1, 'liters', 'cubic_feet'))
    print(convert_volume(10, 'cubic_inches', 'teaspoons'))