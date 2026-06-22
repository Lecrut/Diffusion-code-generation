def convert_volume(volume, source_unit, target_unit='liters'):
    conversion_rates = {
        'liters': 1,
        'milliliters': 0.001,
        'cubic_meters': 1000
    }
    
    if source_unit not in conversion_rates:
        raise ValueError(f"Unsupported source unit: {source_unit}")
    if target_unit not in conversion_rates:
        raise ValueError(f"Unsupported target unit: {target_unit}")
    
    converted_volume = volume * (conversion_rates[source_unit] / conversion_rates[target_unit])
    return converted_volume

if __name__ == '__main__':
    sample_volumes = [
        {'volume': 5, 'source_unit': 'liters', 'target_unit': 'milliliters'},
        {'volume': 2, 'source_unit': 'cubic_meters', 'target_unit': 'liters'},
        {'volume': 1.5, 'source_unit': 'liters', 'target_unit': 'cubic_meters'}
    ]
    
    for sample in sample_volumes:
        converted = convert_volume(sample['volume'], sample['source_unit'], sample['target_unit'])
        print(f"{sample['volume']} {sample['source_unit']} is {converted} {sample['target_unit']}")