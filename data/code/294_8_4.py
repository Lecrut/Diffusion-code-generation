class EquivalentWeightCalculator:
    def __init__(self):
        pass
    def calculate_equivalent_weight(self, mass_A, moles_A, mass_B, moles_B, stoichiometry_ratio):
        if stoichiometry_ratio == 0:
            raise ValueError("Stoichiometry ratio cannot be zero")
        moles_B = moles_A * stoichiometry_ratio
        if moles_A == 0:
            return 0.0
        equivalent_weight = (mass_A / moles_A) * moles_B
        return equivalent_weight
if __name__ == '__main__':
    calculator = EquivalentWeightCalculator()
    mass_A_sample = 10.0         
    moles_A_sample = 2.0         
    mass_B_sample = 5.0          
    moles_B_sample = 4.0         
    stoichiometry_ratio_sample = 1.5
    try:
        result = calculator.calculate_equivalent_weight(
            mass_A_sample, 
            moles_A_sample, 
            mass_B_sample, 
            moles_B_sample, 
            stoichiometry_ratio_sample
        )
        print(f"Equivalent Weight Calculation Result: {result}")
    except ValueError as e:
        print(f"Error: {e}")
    try:
        result_zero = calculator.calculate_equivalent_weight(
            10.0, 
            0.0, 
            5.0, 
            4.0, 
            1.5
        )
        print(f"Equivalent Weight Calculation Result (Zero Moles): {result_zero}")
    except ValueError as e:
        print(f"Error: {e}")