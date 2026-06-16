class CompoundManager:
    def __init__(self):
        self.weights = {}
    def add_compound(self, name, molecular_weight):
        self.weights[name] = molecular_weight
    def calculate_equivalent_weights(self, formula_map):
        equivalent_weights = {}
        for compound_name, mw in self.weights.items():
            if compound_name in formula_map:
                equivalent_weights[compound_name] = mw * formula_map[compound_name]
            else:
                equivalent_weights[compound_name] = None
        return equivalent_weights
if __name__ == '__main__':
    manager = CompoundManager()
    manager.add_compound("Water", 18.015)
    manager.add_compound("Methane", 16.043)
    manager.add_compound("Ethanol", 46.068)
    formula_data = {
        "Water": 2,
        "Methane": 1,
        "Ethanol": 1
    }
    eq_weights = manager.calculate_equivalent_weights(formula_data)
    print("Equivalent Weights:")
    for compound, eq_weight in eq_weights.items():
        print(f"{compound}: {eq_weight}")