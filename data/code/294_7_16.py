def calculate_equivalent_weight(mass):
    molar_mass = 98.08
    oxygen_mass_per_molecule = 3 * 16
    equivalent_weight = (mass / (molar_mass - oxygen_mass_per_molecule)) * molar_mass
    return equivalent_weight

if __name__ == '__main__':
    sample_mass = 98
    print(calculate_equivalent_weight(sample_mass))