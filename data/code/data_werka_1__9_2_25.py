def convert_volume(volume, target_unit):
    conversion_factors = {
        'L': {'m3': 0.001, 'gal': 0.264172},
        'm3': {'L': 1000, 'gal': 264.172},
        'gal': {'L': 3.78541, 'm3': 0.00378541}
    }
    
    if target_unit not in conversion_factors[volume['unit']]:
        raise ValueError("Invalid target unit for conversion")
    
    converted_value = volume['value'] * conversion_factors[volume['unit']][target_unit]
    return {'value': converted_value, 'unit': target_unit}

if __name__ == '__main__':
    sample_volume = {'value': 10, 'unit': 'L'}
    target_unit = 'gal'
    result = convert_volume(sample_volume, target_unit)
    print(result)