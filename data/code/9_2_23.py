def convert_volume(volume, target_unit):
    conversion_factors = {
        'L': {'m3': 0.001, 'gal': 0.264172},
        'm3': {'L': 1000, 'gal': 264.172},
        'gal': {'L': 3.78541, 'm3': 0.00378541}
    }
    
    if target_unit not in conversion_factors:
        raise ValueError("Unsupported target unit")
    
    current_unit = next(iter(conversion_factors))
    if current_unit == target_unit:
        return volume
    
    factor = conversion_factors[current_unit][target_unit]
    converted_volume = volume * factor
    return converted_volume

if __name__ == '__main__':
    sample_volume = 10
    target_unit = 'gal'
    result = convert_volume(sample_volume, target_unit)
    print(result)