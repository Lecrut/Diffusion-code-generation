import numpy as np
def calculate_equivalent_weights(reactions):
    equivalent_weights = {}
    for reaction_id, reaction in reactions.items():
        reactants = reaction['reactants']
        products = reaction['products']
        reactant_moles = {reactant: coeff for reactant, coeff in reactants.items()}
        product_moles = {product: coeff for product, coeff in products.items()}
        total_reactant_mass = sum(reactant_moles.values())
        total_product_mass = sum(product_moles.values())
        if total_reactant_mass == 0 or total_product_mass == 0:
            equivalent_weights[reaction_id] = "Error: Zero mass involved"
            continue
        reactant_sum = sum(reactant_moles.values())
        product_sum = sum(product_moles.values())
        equivalent_weight = reactant_sum + product_sum
        equivalent_weights[reaction_id] = equivalent_weight
    return equivalent_weights
if __name__ == '__main__':
    hypothetical_reactions = {
        "Reaction_A": {
            "reactants": {"H2": 2, "O2": 1},
            "products": {"H2O": 2}
        },
        "Reaction_B": {
            "reactants": {"C": 1, "H2": 2},
            "products": {"CH4": 1, "H2O": 2}
        },
        "Reaction_C": {
            "reactants": {"Al": 1, "H2O": 2},
            "products": {"Al(OH)3": 1, "H2": 3}
        }
    }
    results = calculate_equivalent_weights(hypothetical_reactions)
    print("--- Equivalent Weight Simulation Results ---")
    for reaction_id, weight in results.items():
        print(f"{reaction_id}: {weight}")
    print("------------------------------------------")