def calculate_equivalent_weights(density, volume):
    if density <= 0 or volume <= 0:
        raise ValueError('Density and volume must be positive numbers.')
    return density * volume
if __name__ == '__main__':
    sample_density = 2.5
    sample_volume = 100
    try:
        equivalent_weight = calculate_equivalent_weights(sample_density, sample_volume)
        print(f'Equivalent weight: {equivalent_weight} kg')
    except ValueError as e:
        print(e)