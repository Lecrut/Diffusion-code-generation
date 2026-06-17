import math
def calculate_limiting_reactant_equivalent_weight(reactants, moles, coefficients):
    moles_per_mole = []
    for i in range(len(reactants)):
        moles_per_mole.append(moles[i] * coefficients[i])
    if not moles_per_mole:
        return 0.0
    total_moles = sum(moles_per_mole)
    limiting_reactant_index = -1
    min_moles = float('inf')
    for i in range(len(moles_per_mole)):
        if moles_per_mole[i] < min_moles:
            min_moles = moles_per_mole[i]
            limiting_reactant_index = i
    if limiting_reactant_index != -1:
        return moles_per_mole[limiting_reactant_index] / min_moles
    else:
        return 0.0
if __name__ == '__main__':
    reactants = ["H2", "O2"]
    moles = [1.0, 2.0]
    coefficients = [2, 1]
    result = calculate_limiting_reactant_equivalent_weight(reactants, moles, coefficients)
    print(result)