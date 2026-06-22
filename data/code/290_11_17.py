def calculate_density(mass_kg, volume_m3):
    return mass_kg / volume_m3

if __name__ == '__main__':
    sample_mass_kg = 10.0
    sample_volume_m3 = 2.5
    print(f"Density: {calculate_density(sample_mass_kg, sample_volume_m3)} kg/m^3")