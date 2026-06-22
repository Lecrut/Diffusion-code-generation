def calculate_equivalent_weight(mass1, molar_mass1, mass2, molar_mass2):
    equivalent_weight = (mass1 / molar_mass1) + (mass2 / molar_mass2)
    return equivalent_weight

if __name__ == '__main__':
    weight1 = 50.0
    molar_mass1 = 30.0
    weight2 = 75.0
    molar_mass2 = 40.0
    print(calculate_equivalent_weight(weight1, molar_mass1, weight2, molar_mass2))