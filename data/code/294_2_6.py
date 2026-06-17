class CompoundManager:
    def __init__(self):
        self.compounds = {}
    def add_compound(self, name, molecular_weight, formula):
        self.compounds[name] = {
            "molecular_weight": molecular_weight,
            "formula": formula
        }
    def calculate_equivalent_weight(self, name, molar_mass_of_element):
        if name not in self.compounds:
            return None
        data = self.compounds[name]
        molecular_weight = data["molecular_weight"]
        formula = data["formula"]
        if molar_mass_of_element is None or molar_mass_of_element == 0:
            return None
        try:
            atom_counts = {}
            for element in formula:
                count = formula.count(element)
                atom_counts[element] = atom_counts.get(element, 0) + count
            total_mass = 0
            for element, count in atom_counts.items():
                if element in self.compounds:
                    element_mw = self.compounds[element]["molecular_weight"]
                    total_mass += count * element_mw
            return total_mass / len(formula) if len(formula) > 0 else None
        except Exception:
            return None
if __name__ == '__main__':
    manager = CompoundManager()
    manager.add_compound("Water", 18.015, "H2O")
    manager.add_compound("Methane", 16.043, "CH4")
    manager.add_compound("Glucose", 180.156, "C6H12O6")
    print("--- Compound Data ---")
    print(f"Water MW: {manager.compounds['Water']['molecular_weight']}, Formula: {manager.compounds['Water']['formula']}")
    print(f"Methane MW: {manager.compounds['Methane']['molecular_weight']}, Formula: {manager.compounds['Methane']['formula']}")
    print(f"Glucose MW: {manager.compounds['Glucose']['molecular_weight']}, Formula: {manager.compounds['Glucose']['formula']}")
    print("\n--- Equivalent Weight Calculations (Placeholder based on internal structure) ---")
    h_molar_mass = 1.008         
    water_eqw = manager.calculate_equivalent_weight("Water", h_molar_mass)
    print(f"Equivalent Weight calculation for Water (using H molar mass): {water_eqw}")
    methane_eqw = manager.calculate_equivalent_weight("Methane", 12.011)
    print(f"Equivalent Weight calculation for Methane (using C molar mass): {methane_eqw}")
    glucose_eqw = manager.calculate_equivalent_weight("Glucose", 12.011)
    print(f"Equivalent Weight calculation for Glucose (using C molar mass): {glucose_eqw}")