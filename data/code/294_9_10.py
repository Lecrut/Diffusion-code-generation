class CaOH2Calculator:
    def __init__(self, molar_mass=74.09, oxygen_atomic_mass=16):
        self.molar_mass = molar_mass
        self.oxygen_atomic_mass = oxygen_atomic_mass

    def calculate_equivalent_weight(self, mass):
        return mass / (self.molar_mass - 2 * self.oxygen_atomic_mass)

if __name__ == '__main__':
    calculator = CaOH2Calculator()
    sample_mass = 74
    equivalent_weight = calculator.calculate_equivalent_weight(sample_mass)
    print(equivalent_weight)