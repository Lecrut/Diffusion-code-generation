class MixtureCalculator:
    def __init__(self, molar_mass=74.09, oxygen_mass=16):
        self.molar_mass = molar_mass
        self.oxygen_mass = oxygen_mass

    def calculate_equivalent_weight(self, mass):
        return mass / (self.molar_mass - 2 * self.oxygen_mass)

if __name__ == '__main__':
    calculator = MixtureCalculator()
    sample_mass = 74
    equivalent_weight = calculator.calculate_equivalent_weight(sample_mass)
    print(equivalent_weight)