import numpy as np
def calculate_equivalent_weights(reactions):
    equivalent_weights = {}
    for reaction_id, reaction_data in reactions.items():
        reactants = reaction_data['reactants']
        products = reaction_data['products']
        molar_masses = {
            'H': 1.008, 'O': 15.999, 'C': 12.011, 'Na': 22.990, 'Cl': 35.453
        }
        total_reactant_mass = 0.0
        for element, coefficient in reactants.items():
            if element in molar_masses:
                total_reactant_mass += coefficient * molar_masses[element]
            else:
                pass
        total_product_mass = 0.0
        for element, coefficient in products.items():
            if element in molar_masses:
                total_product_mass += coefficient * molar_masses[element]
            else:
                pass
        if total_reactant_mass > 0:
            ratio = total_product_mass / total_reactant_mass
            equivalent_weights[reaction_id] = ratio
        else:
            equivalent_weights[reaction_id] = np.nan
    return equivalent_weights
if __name__ == '__main__':
    sample_reactions = {
        "Reaction_A": {
            "reactants": {'H': 2, 'O': 1},
            "products": {'H2O': 2}
        },
        "Reaction_B": {
            "reactants": {'Na': 1, 'Cl': 1},
            "products": {'NaCl': 1}
        },
        "Reaction_C": {
            "reactants": {'C': 1, 'H': 2},
            "products": {'CO2': 1, 'H2O': 1}
        }
    }
    results = calculate_equivalent_weights(sample_reactions)
    print("--- Equivalent Weight Simulation Results ---")
    for reaction_id, weight in results.items():
        if np.isnan(weight):
            print(f"{reaction_id}: Calculation failed (Zero reactant mass)")
        else:
            print(f"{reaction_id}: Calculated Mass Ratio (Products/Reactants) = {weight:.4f}")
    print("------------------------------------------")