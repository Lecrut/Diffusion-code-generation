import numpy as np
def calculate_equivalent_weights(reactions):
    results = {}
    for reaction_id, reaction in reactions.items():
        reactants = reaction['reactants']
        products = reaction['products']
        reactant_mass = sum(reactants.values())
        product_mass = sum(products.values())
        if reactant_mass > 0:
            equivalent_weight = product_mass / reactant_mass
        else:
            equivalent_weight = np.nan
        results[reaction_id] = equivalent_weight
    return results
if __name__ == '__main__':
    hypothetical_reactions = {
        "Reaction_A": {
            "reactants": {"H2": 2, "O2": 1},
            "products": {"H2O": 2}
        },
        "Reaction_B": {
            "reactants": {"C": 2, "H2": 1},
            "products": {"CH4": 1}
        },
        "Reaction_C": {
            "reactants": {"Al": 1, "Cl": 1},
            "products": {"AlCl3": 1}
        }
    }
    equivalent_weights = calculate_equivalent_weights(hypothetical_reactions)
    print("Equivalent Weights Simulation Results:")
    for reaction_id, weight in equivalent_weights.items():
        if np.isnan(weight):
            print(f"{reaction_id}: Undefined (Zero Reactant Mass)")
        else:
            print(f"{reaction_id}: {weight:.4f}")