class Substance:
    def __init__(self, mass, molar_mass):
        self.mass = mass
        self.molar_mass = molar_mass

    def calculate_equivalent_weight(self):
        return self.mass * self.molar_mass

if __name__ == '__main__':
    substance1 = Substance(10.0, 44.0)
    substance2 = Substance(5.0, 18.0)
    
    equivalent_weight1 = substance1.calculate_equivalent_weight()
    equivalent_weight2 = substance2.calculate_equivalent_weight()

    total_equivalent_weight = equivalent_weight1 + equivalent_weight2
    print(total_equivalent_weight)