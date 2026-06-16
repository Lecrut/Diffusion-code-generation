def calculate_weighted_average_equivalent_weight(reactants, products):
    total_equivalent_weight = 0
    total_moles = 0
    for reactant, product in zip(reactants, products):
        if reactant is not None and product is not None:
            moles_reactant = reactant
            moles_product = product
            weight = moles_reactant * moles_product
            total_equivalent_weight += weight
            total_moles += moles_reactant
    if total_moles == 0:
        return 0.0
    else:
        weighted_average = total_equivalent_weight / total_moles
        return weighted_average
if __name__ == '__main__':
    reactants_data = [10, 20, 30]
    products_data = [5, 4, 6]
    result = calculate_weighted_average_equivalent_weight(reactants_data, products_data)
    print(result)