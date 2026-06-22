def calculate_equivalent_weight(mass, volume):
    density = mass / volume
    return density
if __name__ == '__main__':
    sample_mass = 100
    sample_volume = 50
    print(calculate_equivalent_weight(sample_mass, sample_volume))