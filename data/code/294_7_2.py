def calculate_weighted_average_equivalent_weight(reactants_and_products):
    total_mass_reactants = 0.0
    total_mass_products = 0.0
    for item in reactants_and_products:
        if 'reactant' in item:
            total_mass_reactants += item['mass']
        elif 'product' in item:
            total_mass_products += item['mass']
    if total_mass_reactants == 0:
        return 0.0
    else:
        weighted_average = (total_mass_products / total_mass_reactants) * 100
        return weighted_average
if __name__ == '__main__':
    sample_data = [
        {'type': 'reactant', 'name': 'Reactant A', 'mass': 50.0},
        {'type': 'reactant', 'name': 'Reactant B', 'mass': 30.0},
        {'type': 'product', 'name': 'Product X', 'mass': 70.0},
        {'type': 'product', 'name': 'Product Y', 'mass': 20.0}
    ]
    weighted_avg = calculate_weighted_average_equivalent_weight(sample_data)
    print(weighted_avg)