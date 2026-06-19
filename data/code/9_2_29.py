def convert_volume(volume, target_unit):
    conversion_factors = {
        'L': {'m3': 0.001, 'gal': 0.264172},
        'm3': {'L': 1000, 'gal': 264.172},
        'gal': {'L': 3.78541, 'm3': 0.00378541}
    }
    
    if target_unit not in conversion_factors[volume['unit']]:
        raise ValueError("Invalid target unit")
    
    converted_value = volume['value'] * conversion_factors[volume['unit']][target_unit]
    return {'value': converted_value, 'unit': target_unit}

if __name__ == '__main__':
    sample_volume1 = {'value': 500, 'unit': 'L'}
    target_unit1 = 'gal'
    result1 = convert_volume(sample_volume1, target_unit1)
    print(result1)

    sample_volume2 = {'value': 2, 'unit': 'm3'}
    target_unit2 = 'L'
    result2 = convert_volume(sample_volume2, target_unit2)
    print(result2)