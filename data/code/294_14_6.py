import numpy as np
def calculate_equivalent_weights(reactions):
    equivalent_weights = {}
    for reaction_id, reaction in reactions.items():
        reactants = reaction['reactants']
        products = reaction['products']
        reactant_moles = {reactant: coeff for reactant, coeff in reactants.items()}
        product_moles = {product: coeff for product, coeff in products.items()}
        total_reactant_coeff = sum(reactant_moles.values())
        total_product_coeff = sum(product_moles.values())
        if total_reactant_coeff == 0 or total_product_coeff == 0:
            equivalent_weights[reaction_id] = "Error: Zero coefficients"
            continue
        reaction_weights = {}
        for substance in reactants.keys() | products.keys():
            coeff = reactant_moles.get(substance, 0) + product_moles.get(substance, 0)
            if coeff != 0:
                reaction_weights[substance] = coeff
        equivalent_weights[reaction_id] = reaction_weights
    return equivalent_weights
if __name__ == '__main__':
    sample_reactions = {
        "Reaction_A": {
            "reactants": {"H2": 2, "O2": 1},
            "products": {"H2O": 2}
        },
        "Reaction_B": {
            "reactants": {"C": 1, "H2": 2},
            "products": {"CH4": 1, "H2O": 1}
        },
        "Reaction_C": {
            "reactants": {"Al": 1, "H2O": 2},
            "products": {"Al(OH)3": 1, "H2": 3}
        }
    }
    results = calculate_equivalent_weights(sample_reactions)
    print("--- Equivalent Weight Simulation Results ---")
    for reaction_id, weights in results.items():
        print(f"\nReaction ID: {reaction_id}")
        if isinstance(weights, dict):
            for substance, weight in weights.items():
                print(f"  Substance {substance}: Equivalent Weight Factor = {weight}")
        else:
            print(f"  Result: {weights}")
    print("------------------------------------------")