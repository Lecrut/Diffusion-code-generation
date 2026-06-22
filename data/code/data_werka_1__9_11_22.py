def convert_volume(value, source_unit, target_unit='liters'):
    conversion_rates = {
        'liters': {'ml': 1000, 'l': 1, 'gal': 0.264172},
        'milliliters': {'ml': 1, 'l': 0.001, 'gal': 0.000264172},
        'gallons': {'ml': 3785.41, 'l': 3.78541, 'gal': 1}
    }
    
    if source_unit not in conversion_rates or target_unit not in conversion_rates[source_unit]:
        raise ValueError("Invalid unit provided")
    
    conversion_factor = conversion_rates[source_unit][target_unit]
    converted_value = value * conversion_factor
    return converted_value

if __name__ == '__main__':
    sample_volume = 5
    source_unit = 'liters'
    target_unit = 'gallons'
    result = convert_volume(sample_volume, source_unit, target_unit)
    print(result)