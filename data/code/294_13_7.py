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
        return reactants[limiting_reactant_index] * (min_total_moles / moles[limiting_reactant_index])
    else:
        return 0.0
if __name__ == '__main__':
    reactants_molar_masses = [2.016, 16.00]                       
    moles_provided = [1.0, 3.0]                      
    coefficients_from_equation = [2, 1]
    equivalent_weight = calculate_limiting_reactant_equivalent_weight(
        reactants=reactants_molar_masses,
        moles=moles_provided,
        coefficients=coefficients_from_equation
    )
    print(equivalent_weight)