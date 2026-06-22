def calculate_weight(density, volume):
    return density * volume
if __name__ == '__main__':
    sample_density = 2.5
    sample_volume = 10
    print(calculate_weight(sample_density, sample_volume))