def calculate_equivalent_weight(mass_h2, mass_o2, molar_mass_h2, molar_mass_o2):
    moles_h2 = mass_h2 / molar_mass_h2
    moles_o2 = mass_o2 / molar_mass_o2
    equivalent_weight = (moles_h2 + 2 * moles_o2) / (moles_h2 + moles_o2)
    return equivalent_weight

if __name__ == '__main__':
    sample_mass_h2 = 2.0
    sample_mass_o2 = 32.0
    sample_molar_mass_h2 = 2.016
    sample_molar_mass_o2 = 32.0
    result = calculate_equivalent_weight(sample_mass_h2, sample_mass_o2, sample_molar_mass_h2, sample_molar_mass_o2)
    print(result)