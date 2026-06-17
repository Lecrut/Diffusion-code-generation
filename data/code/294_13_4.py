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
        reactants_molar_masses = [28.01, 16.00, 32.00, 1.00]
        equivalent_weight = reactants_molar_masses[limiting_reactant_index] * (moles[limiting_reactant_index] * coefficients[limiting_reactant_index])
        return equivalent_weight
    else:
        return 0.0
if __name__ == '__main__':
    reactants = ["H2", "O2"]
    moles = [1.0, 2.0]
    coefficients = [2, 1]
    result = calculate_limiting_reactant_equivalent_weight(reactants, moles, coefficients)
    print(result)