def calculate_density(mass, volume):
    if volume <= 0:
        raise ValueError("Volume must be positive")
    density = mass / volume
    return density
if __name__ == '__main__':
    mass_kg = 100
    volume_m3 = 5.0
    try:
        density_result = calculate_density(mass_kg, volume_m3)
        print(f"Density: {density_result} kg/m^3")
    except ValueError as e:
        print(f"Error: {e}")
    mass_kg_error = 100
    volume_m3_error = -2.0
    try:
        density_result_error = calculate_density(mass_kg_error, volume_m3_error)
        print(f"Density: {density_result_error} kg/m^3")
    except ValueError as e:
        print(f"Error: {e}")