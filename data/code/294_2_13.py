class CompoundManager:
    def __init__(self):
        self.weights = {}

    def add_compound(self, name, molecular_weight):
        self.weights[name] = molecular_weight

    def calculate_equivalent_weights(self, masses, molar_masses):
        equivalent_weights = []
        for mass, molar_mass in zip(masses, molar_masses):
            if molar_mass != 0:
                equivalent_weight = (mass / molar_mass) * molar_mass
                equivalent_weights.append(equivalent_weight)
            else:
                equivalent_weights.append(0)
        return equivalent_weights

if __name__ == '__main__':
    manager = CompoundManager()
    manager.add_compound("Water", 18.015)
    manager.add_compound("Methane", 16.043)
    manager.add_compound("Oxygen", 15.999)

    masses = [2 * 18.015, 1 * 16.043, 3 * 15.999]
    molar_masses = [18.015, 16.043, 15.999]

    print("--- Equivalent Weight Calculations ---")
    print(manager.calculate_equivalent_weights(masses, molar_masses))