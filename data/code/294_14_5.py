import numpy as np
def calculate_equivalent_weights(reactions):
    equivalent_weights = {}
    for reaction_id, reaction in reactions.items():
        reactants = reaction['reactants']
        products = reaction['products']
        moles_reactants = {substance: coeff for substance, coeff in reactants.items()}
        moles_products = {substance: coeff for substance, coeff in products.items()}
        total_reactant_coeff = sum(moles_reactants.values())
        total_product_coeff = sum(moles_products.values())
        if total_reactant_coeff == 0 or total_product_coeff == 0:
            equivalent_weights[reaction_id] = "Error: Zero coefficients"
            continue
        atomic_weights = {
            'H': 1.0, 'O': 16.0, 'C': 12.0, 'Fe': 55.85, 'S': 32.07, 'Na': 22.99, 'Cl': 35.45
        }
        reactant_masses = {}
        for substance, coeff in moles_reactants.items():
            if substance in atomic_weights:
                reactant_masses[substance] = coeff * atomic_weights[substance]
        product_masses = {}
        for substance, coeff in moles_products.items():
            if substance in atomic_weights:
                product_masses[substance] = coeff * atomic_weights[substance]
        total_reactant_mass = sum(reactant_masses.values())
        total_product_mass = sum(product_masses.values())
        if total_product_mass > 0:
            eq_weight = total_reactant_mass / total_product_mass
            equivalent_weights[reaction_id] = eq_weight
        else:
            equivalent_weights[reaction_id] = np.nan
    return equivalent_weights
if __name__ == '__main__':
    sample_reactions = {
        "Reaction_A": {
            "reactants": {"H2": 2, "O2": 1},
            "products": {"H2O": 2}
        },
        "Reaction_B": {
            "reactants": {"Fe": 1, "S": 1},
            "products": {"FeS": 1}
        },
        "Reaction_C": {
            "reactants": {"Na": 2, "Cl": 1},
            "products": {"NaCl": 2}
        }
    }
    results = calculate_equivalent_weights(sample_reactions)
    print("--- Equivalent Weight Calculation Simulation ---")
    for reaction_id, weight in results.items():
        if isinstance(weight, float):
            print(f"Reaction {reaction_id}: Equivalent Weight = {weight:.4f}")
        else:
            print(f"Reaction {reaction_id}: Result = {weight}")
    print("----------------------------------------------")