def calculate_equivalent_weight(mass_H2, mass_O2, molar_mass_H2, molar_mass_O2):
    moles_H2 = mass_H2 / molar_mass_H2
    moles_O2 = mass_O2 / molar_mass_O2
    equivalent_weight = (moles_H2 * 2) + (moles_O2 * 16)
    return equivalent_weight

if __name__ == '__main__':
    sample_mass_H2 = 2.0
    sample_mass_O2 = 32.0
    sample_molar_mass_H2 = 2.016
    sample_molar_mass_O2 = 32.0
    result = calculate_equivalent_weight(sample_mass_H2, sample_mass_O2, sample_molar_mass_H2, sample_molar_mass_O2)
    print(result)