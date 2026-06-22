def validate_masses_and_molar_masses(masses, molar_masses):
    if len(masses) != 3 or len(molar_masses) != 3:
        raise ValueError("Masses and molar masses lists must contain exactly three elements.")
    if any(mass <= 0 for mass in masses) or any(molar_mass <= 0 for molar_mass in molar_masses):
        raise ValueError("All masses and molar masses must be positive.")

def calculate_equivalent_weights(masses, molar_masses):
    validate_masses_and_molar_masses(masses, molar_masses)
    return [mass * (molar_mass / sum(molar_masses)) for mass, molar_mass in zip(masses, molar_masses)]

if __name__ == '__main__':
    masses = [18.015, 16.043, 15.999]
    molar_masses = [18.015, 16.043, 15.999]
    print(calculate_equivalent_weights(masses, molar_masses))