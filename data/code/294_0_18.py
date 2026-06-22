def calculate_equivalent_weight(mass1, mass2, molar_mass1, molar_mass2):
    equivalent_weight1 = mass1 / molar_mass1
    equivalent_weight2 = mass2 / molar_mass2
    total_equivalent_weight = equivalent_weight1 + equivalent_weight2
    return total_equivalent_weight

if __name__ == '__main__':
    mass1 = 10.0
    mass2 = 5.0
    molar_mass1 = 44.0
    molar_mass2 = 18.0
    result = calculate_equivalent_weight(mass1, mass2, molar_mass1, molar_mass2)
    print(result)