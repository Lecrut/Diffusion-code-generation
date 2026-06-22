def convert_volume(volume, source_unit, target_unit='liters'):
    conversion_rates = {
        'liters': {'milliliters': 1000, 'cubic meters': 0.001, 'gallons': 0.264172},
        'milliliters': {'liters': 0.001, 'cubic meters': 0.000001, 'gallons': 0.000264172},
        'cubic meters': {'liters': 1000, 'milliliters': 1000000, 'gallons': 264.172},
        'gallons': {'liters': 3.78541, 'milliliters': 3785.41, 'cubic meters': 0.00378541}
    }
    
    if source_unit not in conversion_rates:
        raise ValueError(f"Unsupported source unit: {source_unit}")
    if target_unit not in conversion_rates[source_unit]:
        raise ValueError(f"Conversion from {source_unit} to {target_unit} is not supported")
    
    return volume * conversion_rates[source_unit][target_unit]

if __name__ == '__main__':
    sample_volume = 5
    source_unit = 'liters'
    target_unit = 'gallons'
    converted_volume = convert_volume(sample_volume, source_unit, target_unit)
    print(converted_volume)