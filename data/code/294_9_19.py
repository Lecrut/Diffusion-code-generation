class WeightCalculator:
    def __init__(self, molar_mass, oxygen_atomic_mass):
        self.molar_mass = molar_mass
        self.oxygen_atomic_mass = oxygen_atomic_mass

    def calculate_equivalent_weight(self, mass):
        return mass / (self.molar_mass - 2 * self.oxygen_atomic_mass)

if __name__ == '__main__':
    calculator = WeightCalculator(74.09, 16)
    sample_mass = 74
    result = calculator.calculate_equivalent_weight(sample_mass)
    print(result)