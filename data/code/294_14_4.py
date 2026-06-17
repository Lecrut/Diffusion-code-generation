import numpy as np
def calculate_equivalent_weights(reactions):
    equivalent_weights = {}
    for reaction_id, reaction_data in reactions.items():
        reactants = reaction_data['reactants']
        products = reaction_data['products']
        reactant_sum = sum(reactants.values())
        product_sum = sum(products.values())
        if reactant_sum > 0:
            weight_ratio = product_sum / reactant_sum if reactant_sum != 0 else np.inf
            equivalent_weights[reaction_id] = weight_ratio
        else:
            equivalent_weights[reaction_id] = 0.0
    return equivalent_weights
if __name__ == '__main__':
    sample_reactions = {
        "R1": {
            "reactants": {"H2": 2, "O2": 1},
            "products": {"H2O": 2}
        },
        "R2": {
            "reactants": {"C": 1, "H2": 2},
            "products": {"CH4": 1}
        },
        "R3": {
            "reactants": {"A": 3, "B": 1},
            "products": {"AB": 1}
        }
    }
    results = calculate_equivalent_weights(sample_reactions)
    print("--- Equivalent Weight Simulation Results ---")
    for reaction_id, weight in results.items():
        print(f"Reaction {reaction_id}: Calculated Ratio/Weight Factor = {weight:.4f}")
    print("------------------------------------------")