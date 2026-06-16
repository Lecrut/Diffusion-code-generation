class CompoundManager:
    def __init__(self):
        self.compound_weights = {}
    def add_compound(self, name, weight):
        self.compound_weights[name] = weight
    def calculate_equivalent_weight(self, name, stoichiometry):
        if name not in self.compound_weights:
            return None
        weight = self.compound_weights[name]
        equivalent_weight = weight * stoichiometry
        return equivalent_weight
if __name__ == '__main__':
    manager = CompoundManager()
    manager.add_compound("H2O", 18.015)
    manager.add_compound("NaCl", 58.44)
    manager.add_compound("C", 12.01)
    print("--- Equivalent Weight Calculations ---")
    try:
        name1 = "H2O"
        stoichiometry1 = 2
        eqw1 = manager.calculate_equivalent_weight(name1, stoichiometry1)
        print(f"Equivalent weight for {name1} with stoichiometry {stoichiometry1}: {eqw1:.3f}")
        name2 = "NaCl"
        stoichiometry2 = 1
        eqw2 = manager.calculate_equivalent_weight(name2, stoichiometry2)
        print(f"Equivalent weight for {name2} with stoichiometry {stoichiometry2}: {eqw2:.3f}")
        name3 = "C"
        stoichiometry3 = 12
        eqw3 = manager.calculate_equivalent_weight(name3, stoichiometry3)
        print(f"Equivalent weight for {name3} with stoichiometry {stoichiometry3}: {eqw3:.3f}")
        name4 = "Unknown"
        stoichiometry4 = 1
        eqw4 = manager.calculate_equivalent_weight(name4, stoichiometry4)
        print(f"Equivalent weight for {name4} with stoichiometry {stoichiometry4}: {eqw4}")
    except Exception as e:
        print(f"An error occurred: {e}")