class EquivalentWeightCalculator:
    def __init__(self):
        pass
    def calculate_equivalent_weight(self, mass_A, moles_A, mass_B, moles_B, stoichiometry_ratio):
        if stoichiometry_ratio == 0:
            raise ValueError("Stoichiometry ratio cannot be zero.")
        moles_B = moles_A * stoichiometry_ratio
        if moles_A == 0:
            return 0.0
        equivalent_weight = (mass_A / moles_A) * moles_B
        return equivalent_weight
if __name__ == '__main__':
    calculator = EquivalentWeightCalculator()
    mass_A_1 = 10.0
    moles_A_1 = 2.0
    mass_B_1 = 5.0
    moles_B_1 = 4.0
    ratio_1 = 2.0
    result_1 = calculator.calculate_equivalent_weight(mass_A_1, moles_A_1, mass_B_1, moles_B_1, ratio_1)
    print(f"Result 1: {result_1}")
    mass_A_2 = 20.0
    moles_A_2 = 1.5
    mass_B_2 = 15.0
    moles_B_2 = 6.0
    ratio_2 = 3.0
    result_2 = calculator.calculate_equivalent_weight(mass_A_2, moles_A_2, mass_B_2, moles_B_2, ratio_2)
    print(f"Result 2: {result_2}")
    mass_A_3 = 10.0
    moles_A_3 = 0.0
    mass_B_3 = 5.0
    moles_B_3 = 4.0
    ratio_3 = 2.0
    result_3 = calculator.calculate_equivalent_weight(mass_A_3, moles_A_3, mass_B_3, moles_B_3, ratio_3)
    print(f"Result 3: {result_3}")