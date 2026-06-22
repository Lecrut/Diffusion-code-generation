def calculate_equivalent_weight(mass, volume):
    if not (isinstance(mass, (int, float)) and isinstance(volume, (int, float))):
        raise ValueError("Mass and volume must be numeric values.")
    if mass <= 0 or volume <= 0:
        raise ValueError("Mass and volume must be positive numbers.")
    return mass / volume

if __name__ == '__main__':
    try:
        sample_mass = 100.0
        sample_volume = 2.5
        equivalent_weight = calculate_equivalent_weight(sample_mass, sample_volume)
        print(f"Equivalent weight: {equivalent_weight}")
        
        invalid_mass = -10.0
        invalid_volume = 2.5
        try:
            calculate_equivalent_weight(invalid_mass, invalid_volume)
        except ValueError as e:
            print(e)

    except Exception as e:
        print(f"An error occurred: {e}")