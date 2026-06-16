class StoichiometryCalculator:
    def calculate_equivalent_weight(self, molar_mass_substance, reaction_stoichiometry_factor):
        return molar_mass_substance * reaction_stoichiometry_factor
if __name__ == '__main__':
    calculator = StoichiometryCalculator()
    molar_mass_h2o = 18.015                   
    stoichiometry_factor_h2o = 2.0                                                                 
    equivalent_weight_water = calculator.calculate_equivalent_weight(molar_mass_h2o, stoichiometry_factor_h2o)
    print(f"Equivalent weight for water (Molar Mass={molar_mass_h2o}, Factor={stoichiometry_factor_h2o}): {equivalent_weight_water}")
    molar_mass_co2 = 44.01                            
    stoichiometry_factor_co2 = 1.0                                                                 
    equivalent_weight_co2 = calculator.calculate_equivalent_weight(molar_mass_co2, stoichiometry_factor_co2)
    print(f"Equivalent weight for CO2 (Molar Mass={molar_mass_co2}, Factor={stoichiometry_factor_co2}): {equivalent_weight_co2}")