def calculate_density(mass_kg: float, volume_m3: float) -> float:
    density_kgm3 = mass_kg / volume_m3
    return density_kgm3

if __name__ == '__main__':
    mass_sample_kg = 7.25
    volume_sample_m3 = 0.45
    print(f"Density of {mass_sample_kg} kg in {volume_sample_m3} m^3 is: {calculate_density(mass_sample_kg, volume_sample_m3)} kg/m^3")