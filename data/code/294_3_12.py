def calculate_equivalent_weight(mass_H2, mass_O2, molar_mass_H2, molar_mass_O2):
    moles_H2 = mass_H2 / molar_mass_H2
    moles_O2 = mass_O2 / molar_mass_O2
    equivalent_weight = (moles_H2 * 2) + (moles_O2 * 16)
    return equivalent_weight

if __name__ == '__main__':
    result = calculate_equivalent_weight(2, 32, 2.016, 32)
    print(result)