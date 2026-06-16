import math
def calculate_density(mass, volume):
    if volume <= 0:
        raise ValueError("Volume must be positive")
    density = mass / volume
    return density
if __name__ == '__main__':
    mass_sample = 100.0
    volume_sample = 2.5
    try:
        density_result = calculate_density(mass_sample, volume_sample)
        print(f"Density: {density_result} kg/m^3")
    except ValueError as e:
        print(f"Error: {e}")
    mass_sample_2 = 50.0
    volume_sample_2 = -1.0
    try:
        density_result_2 = calculate_density(mass_sample_2, volume_sample_2)
        print(f"Density: {density_result_2} kg/m^3")
    except ValueError as e:
        print(f"Error: {e}")
    mass_sample_3 = 0.0
    volume_sample_3 = 1.0
    try:
        density_result_3 = calculate_density(mass_sample_3, volume_sample_3)
        print(f"Density: {density_result_3} kg/m^3")
    except ValueError as e:
        print(f"Error: {e}")