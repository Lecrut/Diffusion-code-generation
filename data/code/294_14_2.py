import numpy as np
def calculate_equivalent_weights(reactions):
    equivalent_weights = {}
    for reaction_id, reaction_data in reactions.items():
        reactants = reaction_data['reactants']
        products = reaction_data['products']
        reactants_mols = [r['moles'] * r['mw'] for r in reactants]
        products_mols = [p['moles'] * p['mw'] for p in products]
        total_reactant_mass = sum(reactants_mols)
        total_product_mass = sum(products_mols)
        if total_reactant_mass > 0:
            mass_change = total_product_mass - total_reactant_mass
            total_moles_reacted = sum(r['moles'] for r in reactants)
            if total_moles_reacted > 0:
                avg_mass_per_mole = total_reactant_mass / total_moles_reacted
                equivalent_weights[reaction_id] = avg_mass_per_mole
            else:
                equivalent_weights[reaction_id] = np.nan
        else:
            equivalent_weights[reaction_id] = np.nan
    return equivalent_weights
if __name__ == '__main__':
    sample_reactions = {
        "Reaction_A": {
            "reactants": [
                {"name": "H2", "moles": 2.0, "mw": 2.016},
                {"name": "O2", "moles": 1.0, "mw": 31.998}
            ],
            "products": [
                {"name": "H2O", "moles": 1.0, "mw": 18.015}
            ]
        },
        "Reaction_B": {
            "reactants": [
                {"name": "C", "moles": 1.0, "mw": 12.011},
                {"name": "H2", "moles": 1.0, "mw": 2.016}
            ],
            "products": [
                {"name": "CH4", "moles": 1.0, "mw": 16.043}
            ]
        },
        "Reaction_C": {
            "reactants": [
                {"name": "Na", "moles": 1.0, "mw": 22.990},
                {"name": "Cl2", "moles": 1.0, "mw": 70.900}
            ],
            "products": [
                {"name": "NaCl", "moles": 1.0, "mw": 58.440}
            ]
        }
    }
    results = calculate_equivalent_weights(sample_reactions)
    print("--- Equivalent Weight Simulation Results ---")
    for reaction_id, ew in results.items():
        print(f"Reaction ID: {reaction_id}")
        if np.isnan(ew):
            print("Equivalent Weight: N/A (No reactants found)")
        else:
            print(f"Calculated Equivalent Weight Proxy: {ew:.4f}")
        print("-" * 30)