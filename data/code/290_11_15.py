CONVERSION_FACTOR_KG_TO_G = 1000
CONVERSION_FACTOR_KG_TO_LB = 2.20462

def calculate_density(mass_kg, volume_m3):
    return mass_kg / volume_m3

if __name__ == '__main__':
    mass_kg_sample = 5.5
    volume_m3_sample = 0.2
    density_kg_per_m3 = calculate_density(mass_kg_sample, volume_m3_sample)
    print(f"Density: {density_kg_per_m3} kg/m^3")