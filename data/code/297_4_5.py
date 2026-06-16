def calculate_density(mass, volume):
    if volume <= 0:
        raise ValueError("Volume must be positive")
    density = mass / volume
    return density
if __name__ == '__main__':
    mass_value = 100.0
    volume_value = 2.5
    try:
        result = calculate_density(mass_value, volume_value)
        print(result)
    except ValueError as e:
        print(f"Error: {e}")
    mass_value = 50.0
    volume_value = -1.0
    try:
        result = calculate_density(mass_value, volume_value)
        print(result)
    except ValueError as e:
        print(f"Error: {e}")
    mass_value = 75.0
    volume_value = 0.0
    try:
        result = calculate_density(mass_value, volume_value)
        print(result)
    except ValueError as e:
        print(f"Error: {e}")