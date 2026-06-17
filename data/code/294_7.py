def calculate_weighted_average_equivalent_weight(reactants, products):
    total_mass = 0
    total_equivalent_weight = 0
    for reactant, product in zip(reactants, products):
        if reactant is not None and product is not None:
            molar_mass_reactant = reactant
            molar_mass_product = product
            total_mass += molar_mass_reactant + molar_mass_product
            total_equivalent_weight += 2 * (molar_mass_reactant * molar_mass_product)
    if len(reactants) > 0:
        weighted_average = total_equivalent_weight / (2 * len(reactants))
        return weighted_average
    else:
        return 0.0
if __name__ == '__main__':
    reactants_masses = [100.0, 50.0]
    products_masses = [110.0, 60.0]
    result = calculate_weighted_average_equivalent_weight(reactants_masses, products_masses)
    print(result)