def calculate_weighted_average_equivalent_weight(reactants, products):
    total_mass_reactants = 0.0
    total_mass_products = 0.0
    for reactant, product in zip(reactants, products):
        total_mass_reactants += reactant
        total_mass_products += product
    if total_mass_reactants == 0:
        return 0.0
    else:
        weighted_average = (total_mass_products / total_mass_reactants) * 100
        return weighted_average
if __name__ == '__main__':
    reactants_data = [10.0, 20.0, 30.0]
    products_data = [15.0, 25.0, 35.0]
    result = calculate_weighted_average_equivalent_weight(reactants_data, products_data)
    print(result)