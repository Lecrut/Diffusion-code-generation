class Mixture:
    def __init__(self, mass_CH4, mass_C, molar_mass_CH4, molar_mass_C):
        self.mass_CH4 = mass_CH4
        self.mass_C = mass_C
        self.molar_mass_CH4 = molar_mass_CH4
        self.molar_mass_C = molar_mass_C

    def calculate_equivalent_weight(self):
        return (self.mass_CH4 * (self.molar_mass_CH4 / 100.0) +
                self.mass_C * (self.molar_mass_C / 100.0))

if __name__ == '__main__':
    mixture = Mixture(16, 12, 16.04, 12.01)
    equivalent_weight = mixture.calculate_equivalent_weight()
    print(f"Equivalent weight of methane and carbon: {equivalent_weight:.2f} g")