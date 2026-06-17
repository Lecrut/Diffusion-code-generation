import math
def calculate_limiting_reactant_equivalent_weight(reactants, moles, coefficients):
    total_moles = sum(moles)
    total_coefficients = sum(coefficients)
    if total_moles == 0:
        return 0.0
    limiting_ratio = total_moles / total_coefficients
    limiting_reactant_index = -1
    min_ratio = float('inf')
    for i, m in enumerate(moles):
        if coefficients[i] != 0:
            current_ratio = m / coefficients[i]
            if current_ratio < min_ratio:
                min_ratio = current_ratio
                limiting_reactant_index = i
    if limiting_reactant_index != -1:
        limiting_reactant_moles = moles[limiting_reactant_index]
        limiting_reactant_mw = reactants[limiting_reactant_index]
        equivalent_weight = limiting_reactant_moles * limiting_reactant_mw
        return equivalent_weight
    else:
        return 0.0
if __name__ == '__main__':
    reactants_list = [100.0, 50.0]
    moles_list = [2.0, 3.0]
    coefficients_list = [1, 2]
    result = calculate_limiting_reactant_equivalent_weight(reactants_list, moles_list, coefficients_list)
    print(result)