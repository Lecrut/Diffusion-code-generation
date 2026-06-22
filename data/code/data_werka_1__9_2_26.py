def convert_volume(volume, target_unit):
    conversion_factors = {
        'L': {'L': 1, 'm3': 0.001, 'gal': 0.264172},
        'm3': {'L': 1000, 'm3': 1, 'gal': 264.172},
        'gal': {'L': 3.78541, 'm3': 0.00378541, 'gal': 1}
    }
    
    if target_unit not in conversion_factors:
        raise ValueError("Unsupported unit")
    
    return volume * conversion_factors[target_unit][target_unit]

if __name__ == '__main__':
    sample_volume = 10
    target_unit = 'm3'
    converted_value = convert_volume(sample_volume, target_unit)
    print(converted_value)