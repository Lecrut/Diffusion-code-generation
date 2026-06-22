class MixtureCalculator:
    def __init__(self, mass_bacl2, molar_mass_bacl2=207.2, atomic_mass_cl=35.45):
        self.mass_bacl2 = mass_bacl2
        self.molar_mass_bacl2 = molar_mass_bacl2
        self.atomic_mass_cl = atomic_mass_cl

    def calculate_equivalent_weight(self):
        return self.mass_bacl2 / (self.molar_mass_bacl2 - 2 * self.atomic_mass_cl)

if __name__ == '__main__':
    calculator = MixtureCalculator(207)
    result = calculator.calculate_equivalent_weight()
    print(result)