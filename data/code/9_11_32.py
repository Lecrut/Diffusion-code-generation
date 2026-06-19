def convert_volume(volume, source_unit, target_unit='liters'):
    conversion_rates = {
        'liters': 1,
        'milliliters': 0.001,
        'cubic_meters': 1000,
        'gallons': 3.78541,
        'quarts': 0.946353,
        'pints': 0.473176,
        'fluid_ounces': 0.0295735
    }
    
    if source_unit not in conversion_rates or target_unit not in conversion_rates:
        raise ValueError("Invalid unit provided")
    
    converted_volume = volume * (conversion_rates[target_unit] / conversion_rates[source_unit])
    return converted_volume

if __name__ == '__main__':
    sample_volume = 5
    sample_source_unit = 'gallons'
    sample_target_unit = 'liters'
    result = convert_volume(sample_volume, sample_source_unit, sample_target_unit)
    print(result)