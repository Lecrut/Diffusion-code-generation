def calculate_density(mass_kg, volume_m3):
    return mass_kg / volume_m3

if __name__ == '__main__':
    density = calculate_density(5.5, 0.2)
    print(f"Density: {density} kg/m^3")