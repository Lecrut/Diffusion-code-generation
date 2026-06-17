import math
def calculate_limiting_reactant_equivalent_weight(reactants, moles, coefficients):
    total_moles = 0.0
    for i in range(len(reactants)):
        total_moles += moles[i] * coefficients[i]
    if total_moles == 0:
        return 0.0
    limiting_reactant_index = -1
    min_total_moles = float('inf')
    for i in range(len(reactants)):
        current_total_moles = moles[i] * coefficients[i]
        if current_total_moles < min_total_moles:
            min_total_moles = current_total_moles
            limiting_reactant_index = i
    if limiting_reactant_index != -1:
        reactants_masses = []
        for i in range(len(reactants)):
            reactants_masses.append(reactants[i])
        return reactants_masses[limiting_reactant_index] * (1 / min_total_moles)
    else:
        return 0.0
if __name__ == '__main__':
    reactants_molar_masses = [100.0, 50.0]                                             
    reactants_moles = [2.0, 1.0]                    
    coefficients = [1, 2]                            
    result = calculate_limiting_reactant_equivalent_weight(reactants_molar_masses, reactants_moles, coefficients)
    print(result)