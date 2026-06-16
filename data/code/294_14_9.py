import numpy as np
def calculate_equivalent_weights(reactions):
    equivalent_weights = {}
    for reaction_id, reaction_data in reactions.items():
        reactants = reaction_data['reactants']
        products = reaction_data['products']
        reactant_sum = sum(reactants.values())
        product_sum = sum(products.values())
        if reactant_sum > 0:
            equivalent_weight = (reactant_sum * 1.0) / product_sum if product_sum > 0 else np.nan
        else:
            equivalent_weight = np.nan
        equivalent_weights[reaction_id] = equivalent_weight
    return equivalent_weights
if __name__ == '__main__':
    sample_reactions = {
        "Reaction_A": {
            "reactants": {"H2": 2, "O2": 1},
            "products": {"H2O": 2}
        },
        "Reaction_B": {
            "reactants": {"C": 1, "H2": 2},
            "products": {"CH4": 1}
        },
        "Reaction_C": {
            "reactants": {"Al": 1, "Cl2": 2},
            "products": {"AlCl3": 3}
        }
    }
    results = calculate_equivalent_weights(sample_reactions)
    print("--- Equivalent Weight Simulation Results ---")
    for reaction_id, weight in results.items():
        if np.isnan(weight):
            print(f"{reaction_id}: Calculation Error (Division by zero or invalid state)")
        else:
            print(f"{reaction_id}: Calculated Equivalent Weight = {weight:.4f}")
    print("------------------------------------------")