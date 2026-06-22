class Compound:
    def __init__(self, name, molar_mass):
        self.name = name
        self.molar_mass = molar_mass

    def calculate_equivalent_weight(self, target_molar_mass):
        return (self.molar_mass / target_molar_mass) * self.molar_mass

class CompoundManager:
    def __init__(self):
        self.compounds = []

    def add_compound(self, compound):
        self.compounds.append(compound)

    def calculate_equivalent_weights(self, target_molar_mass):
        return [compound.calculate_equivalent_weight(target_molar_mass) for compound in self.compounds]

if __name__ == '__main__':
    manager = CompoundManager()
    water = Compound("Water", 18.015)
    methane = Compound("Methane", 16.043)
    oxygen = Compound("Oxygen", 15.999)

    manager.add_compound(water)
    manager.add_compound(methane)
    manager.add_compound(oxygen)

    target_molar_mass = 28.0134
    equivalent_weights = manager.calculate_equivalent_weights(target_molar_mass)
    print(equivalent_weights)