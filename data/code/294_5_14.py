def calculate_equivalent_weight(mass_of_element, molar_mass):
    return mass_of_element * (molar_mass / 100.0)

if __name__ == '__main__':
    mass_of_ch4 = 16.0
    molar_mass_ch4 = 16.04
    mass_of_c = 12.0
    molar_mass_c = 12.01

    equivalent_weight_ch4 = calculate_equivalent_weight(mass_of_ch4, molar_mass_ch4)
    equivalent_weight_c = calculate_equivalent_weight(mass_of_c, molar_mass_c)

    print(f"Equivalent weight of methane (CH4): {equivalent_weight_ch4:.2f} g/mol")
    print(f"Equivalent weight of carbon (C): {equivalent_weight_c:.2f} g/mol")