def convert_volume(volume, target_unit):
    conversion_factors = {'L': {'L': 1, 'm3': 0.001, 'gal': 0.264172}, 'm3': {'L': 1000, 'm3': 1, 'gal': 264.172}, 'gal': {'L': 3.78541, 'm3': 0.00378541, 'gal': 1}}
    if volume < 0:
        raise ValueError('Volume cannot be negative')
    source_unit = 'L'
    return volume * conversion_factors[source_unit][target_unit]
if __name__ == '__main__':
    sample_volume = 10.0
    target_units = ['m3', 'gal']
    for unit in target_units:
        converted_value = convert_volume(sample_volume, unit)
        print(f'{sample_volume} L is {converted_value:.5f} {unit}')