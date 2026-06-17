class CompoundManager:
    def __init__(self):
        self.weights = {}
    def add_compound(self, name, molecular_weight):
        self.weights[name] = molecular_weight
    def calculate_equivalent_weight(self, name, stoichiometry):
        if name not in self.weights:
            return None
        molecular_weight = self.weights[name]
        equivalent_weight = molecular_weight * stoichiometry
        return equivalent_weight
if __name__ == '__main__':
    manager = CompoundManager()
    manager.add_compound("Water", 18.015)
    manager.add_compound("Methane", 16.043)
    manager.add_compound("Oxygen", 15.999)
    print("--- Equivalent Weight Calculations ---")
    compound1 = "Water"
    stoichiometry1 = 2
    ew1 = manager.calculate_equivalent_weight(compound1, stoichiometry1)
    print(f"Equivalent weight for {compound1} (stoichiometry {stoichiometry1}): {ew1}")
    compound2 = "Methane"
    stoichiometry2 = 4
    ew2 = manager.calculate_equivalent_weight(compound2, stoichiometry2)
    print(f"Equivalent weight for {compound2} (stoichiometry {stoichiometry2}): {ew2}")
    compound3 = "Oxygen"
    stoichiometry3 = 1
    ew3 = manager.calculate_equivalent_weight(compound3, stoichiometry3)
    print(f"Equivalent weight for {compound3} (stoichiometry {stoichiometry3}): {ew3}")
    compound4 = "Unknown"
    stoichiometry4 = 2
    ew4 = manager.calculate_equivalent_weight(compound4, stoichiometry4)
    print(f"Equivalent weight for {compound4} (stoichiometry {stoichiometry4}): {ew4}")