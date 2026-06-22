def convert_volume(volume, source_unit, target_unit='liters'):
    conversion_rates = {
        'liters': {'liters': 1, 'milliliters': 1000, 'cubic_meters': 0.001},
        'milliliters': {'liters': 0.001, 'milliliters': 1, 'cubic_meters': 0.000001},
        'cubic_meters': {'liters': 1000, 'milliliters': 1000000, 'cubic_meters': 1}
    }
    
    if source_unit not in conversion_rates:
        raise ValueError(f"Unsupported source unit: {source_unit}")
    if target_unit not in conversion_rates[source_unit]:
        raise ValueError(f"Unsupported target unit from {source_unit}: {target_unit}")
    
    return volume * conversion_rates[source_unit][target_unit]

if __name__ == '__main__':
    sample_volume = 7
    sample_source_unit = 'liters'
    sample_target_unit = 'milliliters'
    converted_volume = convert_volume(sample_volume, sample_source_unit, sample_target_unit)
    print(f"{sample_volume} {sample_source_unit} is equal to {converted_volume} {sample_target_unit}")
    
    another_sample_volume = 3000
    another_sample_source_unit = 'milliliters'
    another_sample_target_unit = 'cubic_meters'
    another_converted_volume = convert_volume(another_sample_volume, another_sample_source_unit, another_sample_target_unit)
    print(f"{another_sample_volume} {another_sample_source_unit} is equal to {another_converted_volume} {another_sample_target_unit}")
    
    yet_another_sample_volume = 1.2
    yet_another_sample_source_unit = 'cubic_meters'
    yet_another_sample_target_unit = 'liters'
    yet_another_converted_volume = convert_volume(yet_another_sample_volume, yet_another_sample_source_unit, yet_another_sample_target_unit)
    print(f"{yet_another_sample_volume} {yet_another_sample_source_unit} is equal to {yet_another_converted_volume} {yet_another_sample_target_unit}")