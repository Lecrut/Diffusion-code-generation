class StoichiometryCalculator:
    def calculate_equivalent_weight(self, molar_mass_reactant, stoichiometry_factor):
        return molar_mass_reactant * stoichiometry_factor
if __name__ == '__main__':
    calculator = StoichiometryCalculator()
    molar_mass_h2o = 18.015                   
    stoichiometry_factor_h2o_to_h2 = 2.0                                             
    equivalent_weight_water = calculator.calculate_equivalent_weight(molar_mass_h2o, stoichiometry_factor_h2o_to_h2)
    print(f"Molar Mass of Water: {molar_mass_h2o} g/mol")
    print(f"Stoichiometry Factor: {stoichiometry_factor_h2o_to_h2}")
    print(f"Equivalent Weight Calculation: {equivalent_weight_water}")