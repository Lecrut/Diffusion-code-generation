def convert_volume_to_liters(volume, unit):
    conversion_factors = {'ml': 0.001, 'cl': 0.01, 'dl': 0.1, 'l': 1.0, 'kl': 1000.0, 'm3': 1000.0, 'cm3': 0.001, 'mm3': 1e-06}
    if unit not in conversion_factors:
        raise ValueError(f'Unsupported unit: {unit}')
    return volume * conversion_factors[unit]
if __name__ == '__main__':
    sample_values = [(500, 'ml'), (2.5, 'l'), (10, 'dl'), (0.0036, 'm3')]
    for volume, unit in sample_values:
        try:
            result = convert_volume_to_liters(volume, unit)
            print(f'{volume} {unit} is equal to {result} liters')
        except ValueError as e:
            print(e)