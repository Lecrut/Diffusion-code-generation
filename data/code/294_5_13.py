MOLAR_MASS_CH4 = 16.04
MOLAR_MASS_C = 12.01

def calculate_equivalent_weight(mass_of_ch4, mass_of_c):
    return (mass_of_ch4 / MOLAR_MASS_CH4) + (mass_of_c / MOLAR_MASS_C)

if __name__ == '__main__':
    mass_of_ch4 = 16.0
    mass_of_c = 12.0
    equivalent_weight = calculate_equivalent_weight(mass_of_ch4, mass_of_c)
    print(f"Equivalent weight of methane and carbon: {equivalent_weight:.2f}")