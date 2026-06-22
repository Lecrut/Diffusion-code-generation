def calculate_equivalent_weights(masses, molar_masses):
    if not all(isinstance(x, (int, float)) and x > 0 for x in masses + molar_masses):
        raise ValueError("All masses and molar masses must be positive numbers.")
    
    return [mass / molar_mass for mass, molar_mass in zip(masses, molar_masses)]

if __name__ == '__main__':
    sample_masses = [18.015, 16.043, 15.999]
    sample_molar_masses = [18.015, 16.043, 15.999]
    result = calculate_equivalent_weights(sample_masses, sample_molar_masses)
    print(result)