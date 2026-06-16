class StoichiometryCalculator:
    def calculate_equivalent_weight(self, molar_mass_substance, reaction_stoichiometry_factor):
        return molar_mass_substance * reaction_stoichiometry_factor
if __name__ == '__main__':
    calculator = StoichiometryCalculator()
    molar_mass_h2o = 18.015                   
    stoichiometry_factor_water = 2.0                                                                 
    equivalent_weight_water = calculator.calculate_equivalent_weight(molar_mass_h2o, stoichiometry_factor_water)
    print(f"Molar Mass of Water: {molar_mass_h2o} g/mol")
    print(f"Reaction Stoichiometry Factor: {stoichiometry_factor_water}")
    print(f"Equivalent Weight of Water (based on factor): {equivalent_weight_water} g/mol")