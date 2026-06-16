class EquivalentWeightCalculator:
    def __init__(self):
        pass
    def calculate_equivalent_weight(self, mass, molar_mass):
        return mass / molar_mass
    def calculate_stoichiometric_equivalence(self, reactant_A, product_B, ratio_A_to_B):
        if ratio_A_to_B <= 0:
            raise ValueError("Ratio must be positive")
        equivalent_weight_A = reactant_A * ratio_A_to_B
        return equivalent_weight_A
class StoichiometryManager:
    def __init__(self):
        self.calculator = EquivalentWeightCalculator()
    def process_reaction(self, reactant_masses, molar_masses, stoichiometric_ratios):
        total_equivalent_weight = 0
        for i in range(len(reactant_masses)):
            reactant_mass = reactant_masses[i]
            molar_mass = molar_masses[i]
            ratio = stoichiometric_ratios[i]
            if ratio <= 0:
                raise ValueError("Stoichiometric ratio must be positive")
            equivalent_weight = self.calculator.calculate_stoichiometric_equivalence(reactant_mass, self.calculator.calculate_equivalent_weight(reactant_mass, molar_mass), ratio)
            total_equivalent_weight += equivalent_weight
        return total_equivalent_weight
if __name__ == '__main__':
    manager = StoichiometryManager()
    reactant_masses = [10.0, 5.0]
    molar_masses = [30.0, 40.0]
    stoichiometric_ratios = [2.0, 1.5]
    try:
        result = manager.process_reaction(reactant_masses, molar_masses, stoichiometric_ratios)
        print(f"Total Stoichiometric Equivalent Weight: {result}")
    except ValueError as e:
        print(f"Error: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")