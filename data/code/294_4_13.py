def calculate_equivalent_weight(mass):
    molar_mass_co2 = 44.01
    atomic_mass_oxygen = 16
    return mass / (molar_mass_co2 - 2 * atomic_mass_oxygen)

if __name__ == '__main__':
    sample_mass = 44
    print(calculate_equivalent_weight(sample_mass))