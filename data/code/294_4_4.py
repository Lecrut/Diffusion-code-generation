def calculate_equivalent_weight(mass):
    molar_mass_co2 = 44.01
    atomic_mass_oxygen = 16
    equivalent_weight = mass / (molar_mass_co2 - 2 * atomic_mass_oxygen)
    return equivalent_weight

if __name__ == '__main__':
    sample_mass = 44
    result = calculate_equivalent_weight(sample_mass)
    print(result)