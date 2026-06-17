def calculate_weighted_average_equivalent_weight(reactants, products):
    total_mass_reactants = 0
    total_mass_products = 0
    for reactant, product in zip(reactants, products):
        if reactant is not None and product is not None:
            total_mass_reactants += reactant
            total_mass_products += product
    if total_mass_reactants == 0:
        return 0.0
    else:
        weighted_average = (total_mass_products / total_mass_reactants) * 100
        return weighted_average
if __name__ == '__main__':
    reactants_data = [100, 200, 300]
    products_data = [150, 250, 350]
    result = calculate_weighted_average_equivalent_weight(reactants_data, products_data)
    print(result)