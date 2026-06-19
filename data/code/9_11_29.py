def convert_volume(volume, source_unit, target_unit='liters'):
    conversion_rates = {
        'liters': {'liters': 1, 'milliliters': 1000, 'cubic_meters': 0.001},
        'milliliters': {'liters': 0.001, 'milliliters': 1, 'cubic_meters': 0.000001},
        'cubic_meters': {'liters': 1000, 'milliliters': 1000000, 'cubic_meters': 1}
    }
    
    if source_unit not in conversion_rates or target_unit not in conversion_rates[source_unit]:
        return "Invalid unit provided"
    
    conversion_factor = conversion_rates[source_unit][target_unit]
    converted_volume = volume * conversion_factor
    return converted_volume

if __name__ == '__main__':
    sample_values = [
        (10, 'liters', 'milliliters'),
        (2.5, 'cubic_meters', 'liters'),
        (500, 'milliliters', 'cubic_meters'),
        (1, 'liters', 'cubic_meters')
    ]
    
    for volume, source_unit, target_unit in sample_values:
        result = convert_volume(volume, source_unit, target_unit)
        print(f"{volume} {source_unit} is equivalent to {result} {target_unit}")