class BariumChloride:
    def __init__(self, mass):
        self.mass = mass
        self.molar_mass_bacl2 = 207.2
        self.atomic_mass_cl = 35.45

    def calculate_equivalent_weight(self):
        return self.mass / (self.molar_mass_bacl2 - 2 * self.atomic_mass_cl)

if __name__ == '__main__':
    sample_mass = 207
    bacl2_instance = BariumChloride(sample_mass)
    equivalent_weight = bacl2_instance.calculate_equivalent_weight()
    print(equivalent_weight)