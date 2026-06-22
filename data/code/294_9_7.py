class CalciumHydroxide:
    def __init__(self, mass):
        self.mass = mass
        self.molar_mass = 74.09
        self.oxygen_atomic_mass = 16

    def calculate_equivalent_weight(self):
        return self.mass / (self.molar_mass - 2 * self.oxygen_atomic_mass)

if __name__ == '__main__':
    sample_mass = 74
    calc_hydroxide = CalciumHydroxide(sample_mass)
    equivalent_weight = calc_hydroxide.calculate_equivalent_weight()
    print(equivalent_weight)