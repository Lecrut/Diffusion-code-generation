def calculate_density(mass_kg, volume_m3):
    return mass_kg / volume_m3
if __name__ == '__main__':
    sample_mass = 50
    sample_volume = 2
    density = calculate_density(sample_mass, sample_volume)
    print(density)