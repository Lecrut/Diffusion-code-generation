def calculate_equivalent_weight(mass):
    molar_mass_h2so4 = 98.08
    atomic_mass_o = 16
    moles_of_o = mass / (molar_mass_h2so4 * 4)
    equivalent_weight = molar_mass_h2so4 / moles_of_o
    return equivalent_weight

if __name__ == '__main__':
    sample_mass = 98.0
    result = calculate_equivalent_weight(sample_mass)
    print(result)