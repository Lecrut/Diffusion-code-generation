def convert_volume(value, source_unit, target_unit='liters'):
    conversion_rates = {
        'liters': {'liters': 1, 'milliliters': 1000, 'cubic_meters': 0.001},
        'milliliters': {'liters': 0.001, 'milliliters': 1, 'cubic_meters': 0.000001},
        'cubic_meters': {'liters': 1000, 'milliliters': 1000000, 'cubic_meters': 1}
    }
    
    if source_unit not in conversion_rates or target_unit not in conversion_rates[source_unit]:
        raise ValueError("Invalid unit specified")
    
    return value * conversion_rates[source_unit][target_unit]

if __name__ == '__main__':
    sample_value = 5
    sample_source_unit = 'liters'
    sample_target_unit = 'milliliters'
    result = convert_volume(sample_value, sample_source_unit, sample_target_unit)
    print(result)