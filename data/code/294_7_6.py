def calculate_weighted_average_equivalent_weight(reactants, products):
    total_equivalent_weight = 0
    total_moles = 0
    for reactant, product in zip(reactants, products):
        if reactant is not None and product is not None:
            molar_mass_reactant = reactant
            molar_mass_product = product
            weight = molar_mass_reactant * molar_mass_product
            total_equivalent_weight += weight
            total_moles += 1                 
    if total_moles == 0:
        return 0.0
    weighted_average = total_equivalent_weight / total_moles
    return weighted_average
if __name__ == '__main__':
    reactants_data = [100.0, 50.0]
    products_data = [200.0, 300.0]
    result = calculate_weighted_average_equivalent_weight(reactants_data, products_data)
    print(result)