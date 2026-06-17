class CompoundManager:
    def __init__(self):
        self.compounds = {}
    def add_compound(self, name, molecular_weight):
        self.compounds[name] = molecular_weight
    def calculate_equivalent_weights(self, compound_name, stoichiometry):
        if compound_name not in self.compounds:
            return None
        molecular_weight = self.compounds[compound_name]
        equivalent_weight = molecular_weight * stoichiometry
        return equivalent_weight
if __name__ == '__main__':
    manager = CompoundManager()
    manager.add_compound("Water", 18.015)
    manager.add_compound("Methane", 16.043)
    manager.add_compound("Carbon Dioxide", 44.01)
    print("--- Equivalent Weight Calculations ---")
    compound1 = "Water"
    stoichiometry1 = 2
    ew1 = manager.calculate_equivalent_weights(compound1, stoichiometry1)
    print(f"Equivalent weight of {compound1} for stoichiometry {stoichiometry1}: {ew1}")
    compound2 = "Methane"
    stoichiometry2 = 1
    ew2 = manager.calculate_equivalent_weights(compound2, stoichiometry2)
    print(f"Equivalent weight of {compound2} for stoichiometry {stoichiometry2}: {ew2}")
    compound3 = "Carbon Dioxide"
    stoichiometry3 = 1
    ew3 = manager.calculate_equivalent_weights(compound3, stoichiometry3)
    print(f"Equivalent weight of {compound3} for stoichiometry {stoichiometry3}: {ew3}")
    compound4 = "Unknown"
    stoichiometry4 = 1
    ew4 = manager.calculate_equivalent_weights(compound4, stoichiometry4)
    print(f"Equivalent weight of {compound4} for stoichiometry {stoichiometry4}: {ew4}")