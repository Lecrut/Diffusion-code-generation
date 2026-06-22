class CalciumHydroxideCalculator:
    def __init__(self):
        self.molar_mass = 74.09
        self.oxygen_atomic_mass = 16

    def calculate_equivalent_weight(self, mass):
        return mass / (self.molar_mass - 2 * self.oxygen_atomic_mass)

if __name__ == '__main__':
    calculator = CalciumHydroxideCalculator()
    sample_mass = 74
    equivalent_weight = calculator.calculate_equivalent_weight(sample_mass)
    print(equivalent_weight)