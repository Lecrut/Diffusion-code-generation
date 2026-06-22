def calculate_equivalent_weight(mass_ch4, mass_c, molar_mass_ch4, molar_mass_c):
    moles_ch4 = mass_ch4 / molar_mass_ch4
    moles_c = mass_c / molar_mass_c
    equivalent_weight = (moles_ch4 * 16) + (moles_c * 12)
    return equivalent_weight

if __name__ == '__main__':
    mass_ch4 = 16.04
    mass_c = 12.01
    molar_mass_ch4 = 16.04
    molar_mass_c = 12.01
    print(calculate_equivalent_weight(mass_ch4, mass_c, molar_mass_ch4, molar_mass_c))