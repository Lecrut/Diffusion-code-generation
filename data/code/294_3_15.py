def calculate_molar_mass(mass, moles):
    if mass < 0 or moles <= 0:
        raise ValueError("Mass must be non-negative and moles must be positive.")
    return mass / moles

def calculate_equivalent_weight(molar_mass, molar_mass_oxygen):
    return molar_mass * (molar_mass_oxygen / (2 * molar_mass + molar_mass_oxygen))

if __name__ == '__main__':
    hydrogen_mass = 2.0
    oxygen_mass = 32.0
    try:
        hydrogen_moles = calculate_molar_mass(hydrogen_mass, 1.0)
        oxygen_moles = calculate_molar_mass(oxygen_mass, 1.0)
        equivalent_weight = calculate_equivalent_weight(hydrogen_moles, oxygen_moles)
        print(f"Equivalent weight of the mixture: {equivalent_weight:.4f}")
    except ValueError as e:
        print(f"Error: {e}")