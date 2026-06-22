def convert_volume(volume, source_unit, target_unit='liters'):
    conversion_rates = {
        'liters': {'liters': 1, 'milliliters': 1000, 'cubic_meters': 0.001},
        'milliliters': {'liters': 0.001, 'milliliters': 1, 'cubic_meters': 1e-6},
        'cubic_meters': {'liters': 1000, 'milliliters': 1000000, 'cubic_meters': 1}
    }
    
    if not isinstance(volume, (int, float)):
        raise TypeError("Volume must be a number.")
    
    if source_unit not in conversion_rates:
        raise ValueError(f"Unsupported source unit: {source_unit}")
    
    if target_unit not in conversion_rates[source_unit]:
        raise ValueError(f"Unsupported target unit from {source_unit}: {target_unit}")
    
    return volume * conversion_rates[source_unit][target_unit]

if __name__ == '__main__':
    try:
        sample_volume = 7.5
        sample_source_unit = 'cubic_meters'
        sample_target_unit = 'liters'
        converted_volume = convert_volume(sample_volume, sample_source_unit, sample_target_unit)
        print(converted_volume)
        
        another_sample_volume = 2000
        another_sample_source_unit = 'milliliters'
        another_sample_target_unit = 'cubic_meters'
        another_converted_volume = convert_volume(another_sample_volume, another_sample_source_unit, another_sample_target_unit)
        print(another_converted_volume)
        
    except Exception as e:
        print(f"Error: {e}")