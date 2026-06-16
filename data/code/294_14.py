import numpy as np
def calculate_equivalent_weights(reactions):
    equivalent_weights = {}
    for reaction_id, reaction_data in reactions.items():
        reactants = reaction_data['reactants']
        products = reaction_data['products']
        moles_reactants = {reactant: moles for reactant, moles in reactants.items()}
        moles_products = {product: moles for product, moles in products.items()}
        total_reactant_moles = sum(moles_reactants.values())
        if total_reactant_moles > 0:
            equivalent_weight = total_reactant_moles 
        else:
            equivalent_weight = 0
        equivalent_weights[reaction_id] = equivalent_weight
    return equivalent_weights
if __name__ == '__main__':
    hypothetical_reactions = {
        "R1": {
            "reactants": {"A": 2.0, "B": 1.5},
            "products": {"C": 3.0}
        },
        "R2": {
            "reactants": {"D": 4.0, "E": 0.5},
            "products": {"F": 6.0}
        },
        "R3": {
            "reactants": {"A": 1.0, "B": 2.0},
            "products": {"C": 2.0}
        }
    }
    results = calculate_equivalent_weights(hypothetical_reactions)
    print("--- Equivalent Weight Simulation Results ---")
    for reaction_id, weight in results.items():
        print(f"Reaction {reaction_id}: Equivalent Weight = {weight}")
    print("------------------------------------------")