def calculate_equivalent_weight(mass_ch4, mass_c, molar_mass_ch4, molar_mass_c):
    moles_ch4 = mass_ch4 / molar_mass_ch4
    moles_c = mass_c / molar_mass_c
    equivalent_weight = (moles_ch4 * molar_mass_ch4 + moles_c * molar_mass_c) / (moles_ch4 + moles_c)
    return equivalent_weight

if __name__ == '__main__':
    mass_ch4 = 16.0
    mass_c = 12.0
    molar_mass_ch4 = 16.04
    molar_mass_c = 12.01
    print(calculate_equivalent_weight(mass_ch4, mass_c, molar_mass_ch4, molar_mass_c))