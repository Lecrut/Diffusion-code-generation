def calculate_equivalent_weights(mass1, mass2, mass3, molar_mass1, molar_mass2, molar_mass3):
    equivalent_weight1 = (mass1 / molar_mass1) * 1000
    equivalent_weight2 = (mass2 / molar_mass2) * 1000
    equivalent_weight3 = (mass3 / molar_mass3) * 1000
    return [equivalent_weight1, equivalent_weight2, equivalent_weight3]

if __name__ == '__main__':
    result = calculate_equivalent_weights(18.015, 16.043, 15.999, 18.015, 16.043, 15.999)
    print(result)