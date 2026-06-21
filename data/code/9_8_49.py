def convert_volume(volume, source_unit, target_unit='liters'):
    conversion_rates = {
        'liters': {'liters': 1, 'milliliters': 1000, 'cubic_meters': 0.001},
        'milliliters': {'liters': 0.001, 'milliliters': 1, 'cubic_meters': 1e-06},
        'cubic_meters': {'liters': 1000, 'milliliters': 1000000, 'cubic_meters': 1}
    }
    
    if not isinstance(volume, (int, float)):
        raise ValueError("Volume must be a number.")
    
    if source_unit not in conversion_rates:
        raise ValueError(f"Unsupported source unit: {source_unit}")
    
    if target_unit not in conversion_rates[source_unit]:
        raise ValueError(f"Unsupported target unit from {source_unit}: {target_unit}")
    
    return volume * conversion_rates[source_unit][target_unit]

if __name__ == '__main__':
    try:
        sample_volume = 10
        sample_source_unit = 'cubic_meters'
        sample_target_unit = 'liters'
        converted_volume = convert_volume(sample_volume, sample_source_unit, sample_target_unit)
        print(converted_volume)
        
        sample_volume = 500
        sample_source_unit = 'milliliters'
        sample_target_unit = 'cubic_meters'
        converted_volume = convert_volume(sample_volume, sample_source_unit, sample_target_unit)
        print(converted_volume)
        
        sample_volume = 2.5
        sample_source_unit = 'liters'
        sample_target_unit = 'milliliters'
        converted_volume = convert_volume(sample_volume, sample_source_unit, sample_target_unit)
        print(converted_volume)
    except ValueError as e:
        print(e)