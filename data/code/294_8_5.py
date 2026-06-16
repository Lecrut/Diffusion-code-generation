class EquivalentWeightCalculator:
    def __init__(self):
        pass
    def calculate_equivalent_weight(self, mass, molar_mass):
        return mass / molar_mass
    def calculate_stoichiometric_equivalence(self, substance_a, substance_b, ratio_a, ratio_b):
        if ratio_a == 0 or ratio_b == 0:
            raise ValueError("Ratios cannot be zero")
        moles_a = substance_a * ratio_a
        moles_b = substance_b * ratio_b
        total_mass = moles_a * 100                                          
        total_mass += moles_b * 50                                          
        if total_mass == 0:
            return 0.0
        equivalent_weight = total_mass / (moles_a + moles_b)
        return equivalent_weight
if __name__ == '__main__':
    calculator = EquivalentWeightCalculator()
    mass_a = 100.0
    molar_mass_a = 50.0
    mass_b = 200.0
    molar_mass_b = 75.0
    ratio_a = 2.0
    ratio_b = 3.0
    try:
        eq_weight = calculator.calculate_stoichiometric_equivalence(mass_a, mass_b, ratio_a, ratio_b)
        print(f"Mass A: {mass_a}, Molar Mass A: {molar_mass_a}")
        print(f"Mass B: {mass_b}, Molar Mass B: {molar_mass_b}")
        print(f"Ratio A: {ratio_a}, Ratio B: {ratio_b}")
        print(f"Calculated Stoichiometric Equivalent Weight: {eq_weight}")
    except ValueError as e:
        print(f"Error: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")