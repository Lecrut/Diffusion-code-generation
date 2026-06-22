def calculate_equivalent_weight(mass):
    molar_mass = 98.08
    oxygen_mass = 16 * 4
    equivalent_weight = (mass / (molar_mass - oxygen_mass)) * molar_mass
    return equivalent_weight

if __name__ == '__main__':
    sample_mass = 98
    print(calculate_equivalent_weight(sample_mass))