def calculate_equivalent_weights(mass1, molar_mass1, mass2, molar_mass2, mass3, molar_mass3):
    if any(isinstance(x, str) for x in [mass1, mass2, mass3]):
        raise ValueError("Mass values must be numeric.")
    if any(isinstance(x, str) for x in [molar_mass1, molar_mass2, molar_mass3]):
        raise ValueError("Molar mass values must be numeric.")
    
    weights = []
    total_weight = mass1 + mass2 + mass3
    for mass, molar_mass in [(mass1, molar_mass1), (mass2, molar_mass2), (mass3, molar_mass3)]:
        if molar_mass == 0:
            raise ValueError("Molar mass cannot be zero.")
        equivalent_weight = mass * (total_weight / molar_mass)
        weights.append(equivalent_weight)
    
    return weights

if __name__ == '__main__':
    print(calculate_equivalent_weights(18.015, 1, 16.043, 1, 15.999, 1))