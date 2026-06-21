def convert_volume(value, source_unit, target_unit='liters'):
    conversions_to_liters = {
        'liters': 1.0,
        'milliliters': 0.001,
        'gallons_us': 3.78541,
        'quarts_us': 0.946353,
        'pints_us': 0.473176,
        'cups_us': 0.236588,
        'fluid_ounces_us': 0.0295735,
        'tablespoons_us': 0.0147868,
        'teaspoons_us': 0.00492892,
        'cubic_meters': 1000.0,
        'cubic_centimeters': 0.001,
        'liters_uk': 1.13652,
        'gallons_uk': 1.13652 * 4.54609,
        'quarts_uk': 1.13652,
        'pints_uk': 0.568261
    }
    
    if source_unit not in conversions_to_liters:
        raise ValueError(f"Invalid source unit: {source_unit}")
    if target_unit not in conversions_to_liters:
        raise ValueError(f"Invalid target unit: {target_unit}")
    
    value_in_liters = value * conversions_to_liters[source_unit]
    result = value_in_liters / conversions_to_liters[target_unit]
    return result

if __name__ == '__main__':
    print(convert_volume(1, 'gallons_us', 'liters'))
    print(convert_volume(1000, 'milliliters', 'liters'))
    print(convert_volume(5, 'liters', 'gallons_us'))