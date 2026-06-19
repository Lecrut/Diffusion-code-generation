def convert_volume(volume, target_unit):
    conversion_factors = {
        'L': 1.0,
        'm3': 0.001,
        'gal': 0.264172,
        'qt': 1.05669,
        'pt': 2.11338,
        'fl oz': 33.814
    }
    
    base_unit = 'L'
    if base_unit == target_unit:
        return volume
    
    base_volume = volume * conversion_factors[base_unit]
    converted_volume = base_volume / conversion_factors[target_unit]
    return converted_volume

if __name__ == '__main__':
    sample_volume = 10
    target_units = ['m3', 'gal', 'qt', 'pt', 'fl oz']
    
    for unit in target_units:
        print(f"{sample_volume} L is {convert_volume(sample_volume, unit)} {unit}")