class WaterEquivalentWeightCalculator:

    def __init__(self):
        self.water_molar_mass = 18.015

    def calculate_equivalent_weight(self, mass):
        return mass / self.water_molar_mass
if __name__ == '__main__':
    calculator = WaterEquivalentWeightCalculator()
    water_mass = 18.0
    equivalent_weight = calculator.calculate_equivalent_weight(water_mass)
    print(equivalent_weight)