class BariumChlorideMixture:
    def __init__(self, mass_bacl2):
        self.mass_bacl2 = mass_bacl2
        self.molar_mass_bacl2 = 207.2
        self.atomic_mass_cl = 35.45

    def calculate_equivalent_weight(self):
        equivalent_weight = self.mass_bacl2 / (self.molar_mass_bacl2 - 2 * self.atomic_mass_cl)
        return equivalent_weight

if __name__ == '__main__':
    sample_mass = 207
    mixture = BariumChlorideMixture(sample_mass)
    result = mixture.calculate_equivalent_weight()
    print(result)