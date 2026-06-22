def validate_masses_and_molar_masses(mass1, mass2, mass3, molar_mass1, molar_mass2, molar_mass3):
    if not all(isinstance(val, (int, float)) for val in [mass1, mass2, mass3, molar_mass1, molar_mass2, molar_mass3]):
        raise ValueError("All inputs must be numeric.")
    if any(mass <= 0 or molar_mass <= 0 for mass, molar_mass in zip([mass1, mass2, mass3], [molar_mass1, molar_mass2, molar_mass3])):
        raise ValueError("Masses and molar masses must be positive.")

def calculate_equivalent_weights(mass1, mass2, mass3, molar_mass1, molar_mass2, molar_mass3):
    validate_masses_and_molar_masses(mass1, mass2, mass3, molar_mass1, molar_mass2, molar_mass3)
    
    weights = [
        (mass1 / molar_mass1),
        (mass2 / molar_mass2),
        (mass3 / molar_mass3)
    ]
    
    return weights

if __name__ == '__main__':
    mass1, mass2, mass3 = 5.0, 10.0, 7.5
    molar_mass1, molar_mass2, molar_mass3 = 18.015, 16.043, 15.999
    
    equivalent_weights = calculate_equivalent_weights(mass1, mass2, mass3, molar_mass1, molar_mass2, molar_mass3)
    
    print(equivalent_weights)