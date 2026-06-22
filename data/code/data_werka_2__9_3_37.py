def convert_to_liters(volume, unit):
    conversion_factors = {'ml': 0.001, 'cl': 0.01, 'dl': 0.1, 'l': 1.0, 'kl': 1000.0, 'm3': 1000.0, 'cm3': 0.001, 'mm3': 1e-06}
    if unit not in conversion_factors:
        raise ValueError(f'Unsupported unit: {unit}')
    return volume * conversion_factors[unit]
if __name__ == '__main__':
    sample_values = [(500, 'ml'), (2, 'l'), (1.5, 'kl'), (300, 'cm3'), (1000, 'mm3')]
    for volume, unit in sample_values:
        liters = convert_to_liters(volume, unit)
        print(f'{volume} {unit} is equal to {liters} liters')