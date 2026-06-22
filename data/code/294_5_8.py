def calculate_equivalent_weight(mass_ch4, mass_c, molar_mass_ch4, molar_mass_c):
    moles_ch4 = mass_ch4 / molar_mass_ch4
    moles_c = mass_c / molar_mass_c
    equivalent_weight = (moles_ch4 * molar_mass_ch4 + moles_c * molar_mass_c) / (moles_ch4 + moles_c)
    return equivalent_weight

if __name__ == '__main__':
    print(calculate_equivalent_weight(16, 12, 16.04, 12.01))