def convert_volume(volume, source_unit, target_unit='liters'):
    conversion_rates = {
        'liters': {'liters': 1, 'milliliters': 1000, 'cubic_meters': 0.001},
        'milliliters': {'liters': 0.001, 'milliliters': 1, 'cubic_meters': 0.000001},
        'cubic_meters': {'liters': 1000, 'milliliters': 1000000, 'cubic_meters': 1}
    }
    
    if source_unit not in conversion_rates or target_unit not in conversion_rates[source_unit]:
        return "Invalid unit conversion"
    
    conversion_factor = conversion_rates[source_unit][target_unit]
    converted_volume = volume * conversion_factor
    return converted_volume

if __name__ == '__main__':
    sample_volume = 500
    sample_source_unit = 'milliliters'
    sample_target_unit = 'liters'
    result = convert_volume(sample_volume, sample_source_unit, sample_target_unit)
    print(result)