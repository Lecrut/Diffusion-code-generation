def calculate_density(mass, volume):
    return mass / volume
if __name__ == '__main__':
    sample_mass = 50
    sample_volume = 2
    density = calculate_density(sample_mass, sample_volume)
    print(density)