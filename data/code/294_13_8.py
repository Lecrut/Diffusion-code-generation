def calculate_equivalent_weight(mass, volume):
    density = mass / volume
    return density
if __name__ == '__main__':
    sample_mass = 50
    sample_volume = 10
    equivalent_weight = calculate_equivalent_weight(sample_mass, sample_volume)
    print(equivalent_weight)