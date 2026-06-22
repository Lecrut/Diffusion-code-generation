def calculate_equivalent_weight(nh3_mass, h_mass):
    nh3_molar_mass = 17.03
    h_molar_mass = 1.01
    nh3_moles = nh3_mass / nh3_molar_mass
    h_moles = h_mass / h_molar_mass
    equivalent_weight = (nh3_moles + h_moles) * nh3_molar_mass
    return equivalent_weight

if __name__ == '__main__':
    print(calculate_equivalent_weight(17, 2))