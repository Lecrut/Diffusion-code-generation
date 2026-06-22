def calculate_density(mass_kg, volume_m3):
    return mass_kg / volume_m3

if __name__ == '__main__':
    mass_kg_sample = 5.5
    volume_m3_sample = 0.25
    print(f"Density of {mass_kg_sample} kg in {volume_m3_sample} m³ is: {calculate_density(mass_kg_sample, volume_m3_sample)} kg/m³")