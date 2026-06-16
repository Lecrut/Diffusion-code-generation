import numpy as np
def calculate_equivalent_weights(reactions):
    results = {}
    for reaction_id, reaction in reactions.items():
        reactants = reaction['reactants']
        products = reaction['products']
        reactant_masses = sum(reactants.values())
        product_masses = sum(products.values())
        if reactant_masses > 0:
            equivalent_weight = product_masses / reactant_masses
        else:
            equivalent_weight = np.nan
        results[reaction_id] = {
            'reactants': reactants,
            'products': products,
            'equivalent_weight': equivalent_weight
        }
    return results
if __name__ == '__main__':
    sample_reactions = {
        "Reaction_A": {
            "reactants": {"H2": 2.0, "O2": 1.0},
            "products": {"H2O": 1.0}
        },
        "Reaction_B": {
            "reactants": {"C": 1.0, "H2": 2.0},
            "products": {"CH4": 1.0}
        },
        "Reaction_C": {
            "reactants": {"Al": 1.0, "Si": 1.0},
            "products": {"AlSi": 1.0}
        }
    }
    calculated_results = calculate_equivalent_weights(sample_reactions)
    print("--- Equivalent Weight Calculation Simulation ---")
    for reaction_id, data in calculated_results.items():
        print(f"\nReaction ID: {reaction_id}")
        print(f"  Reactants (Mass/Coefficient): {data['reactants']}")
        print(f"  Products (Mass/Coefficient): {data['products']}")
        print(f"  Calculated Equivalent Weight Ratio: {data['equivalent_weight']:.4f}")
    print("\n---------------------------------------------")