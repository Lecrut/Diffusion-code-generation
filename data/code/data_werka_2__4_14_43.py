def normalize_distance(value, unit):
    conversion_factors = {'meters': 1, 'kilometers': 1000, 'miles': 1609.34}
    if unit not in conversion_factors:
        raise ValueError(f'Unsupported unit: {unit}')
    meters = value * conversion_factors[unit]
    return meters
if __name__ == '__main__':
    distances = [(10, 'meters'), (5, 'kilometers'), (2, 'miles')]
    for value, unit in distances:
        normalized_value = normalize_distance(value, unit)
        print(f'{value} {unit} is {normalized_value} meters')