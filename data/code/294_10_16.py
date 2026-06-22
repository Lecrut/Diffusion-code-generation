def calculate_equivalent_weight(density, volume):
    if density <= 0 or volume <= 0:
        raise ValueError('Density and volume must be positive numbers.')
    return density * volume
if __name__ == '__main__':
    sample_density = 2.7
    sample_volume = 100
    try:
        result = calculate_equivalent_weight(sample_density, sample_volume)
        print(f'Equivalent weight: {result} grams')
    except ValueError as e:
        print(e)