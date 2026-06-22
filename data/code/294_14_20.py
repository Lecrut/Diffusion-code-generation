def calculate_weight(density, volume):
    return density * volume
if __name__ == '__main__':
    sample_density = 2500
    sample_volume = 0.1
    print(calculate_weight(sample_density, sample_volume))