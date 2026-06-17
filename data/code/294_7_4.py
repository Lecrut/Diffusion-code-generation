def calculate_weighted_average_equivalent_weight(reactants, products):
    total_mass_reactants = 0
    total_mass_products = 0
    for reactant, product in zip(reactants, products):
        if isinstance(reactant, dict) and isinstance(product, dict):
            molar_mass_reactant = reactant.get('molar_mass', 1.0)
            moles_reactant = reactant.get('moles', 1.0)
            molar_mass_product = product.get('molar_mass', 1.0)
            moles_product = product.get('moles', 1.0)
            total_mass_reactants += moles_reactant * molar_mass_reactant
            total_mass_products += moles_product * molar_mass_product
        else:
            raise ValueError("Input data must be a list of dictionaries with 'moles' and 'molar_mass' keys.")
    if total_mass_reactants == 0:
        return 0.0
    weighted_average = (total_mass_products / total_mass_reactants) * 100
    return weighted_average
if __name__ == '__main__':
    reactants_data = [
        {'name': 'Reactant A', 'moles': 2.0, 'molar_mass': 50.0},
        {'name': 'Reactant B', 'moles': 1.0, 'molar_mass': 100.0}
    ]
    products_data = [
        {'name': 'Product X', 'moles': 3.0, 'molar_mass': 75.0},
        {'name': 'Product Y', 'moles': 2.0, 'molar_mass': 150.0}
    ]
    try:
        weighted_avg = calculate_weighted_average_equivalent_weight(reactants_data, products_data)
        print(f"Weighted Average Equivalent Weight: {weighted_avg}")
    except ValueError as e:
        print(f"Error: {e}")