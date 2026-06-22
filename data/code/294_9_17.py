def calculate_equivalent_weight(mass):
    molar_mass = 74.09
    oxygen_mass = 16 * 2
    equivalent_weight = mass / (molar_mass - oxygen_mass)
    return equivalent_weight

if __name__ == '__main__':
    sample_mass = 74
    print(calculate_equivalent_weight(sample_mass))