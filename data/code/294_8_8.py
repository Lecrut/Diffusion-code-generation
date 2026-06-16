class EquivalentWeightCalculator:
    def __init__(self):
        pass
    def calculate_equivalent_weight(self, mass, molar_mass):
        return mass / molar_mass
    def calculate_stoichiometric_equivalence(self, reactant_A_mass, product_B_mass, ratio_A_to_B):
        if ratio_A_to_B == 0:
            raise ValueError("Ratio cannot be zero")
        moles_A = reactant_A_mass / 100.0                                                                                                          
        theoretical_mass_B = moles_A * ratio_A_to_B
        return theoretical_mass_B
if __name__ == '__main__':
    calculator = EquivalentWeightCalculator()
    reactant_A_mass = 50.0                       
    product_B_mass_actual = 125.0                                                     
    stoichiometric_ratio = 2.0                                                                                
    print(f"Reactant A Mass: {reactant_A_mass} g")
    print(f"Product B Actual Mass: {product_B_mass_actual} g")
    print(f"Stoichiometric Ratio (A to B): {stoichiometric_ratio}")
    try:
        theoretical_mass_B = calculator.calculate_stoichiometric_equivalence(reactant_A_mass, product_B_mass_actual, stoichiometric_ratio)
        print(f"\nTheoretical Mass of Product B based on ratio and A mass: {theoretical_mass_B:.2f} g")
    except ValueError as e:
        print(f"Error: {e}")
    mass_A = 10.0
    molar_mass_A = 50.0
    eq_weight_A = calculator.calculate_equivalent_weight(mass_A, molar_mass_A)
    print(f"\nEquivalent Weight of A (Mass / Molar Mass): {eq_weight_A:.2f}")