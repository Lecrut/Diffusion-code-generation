class StoichiometryCalculator:
    def calculate_equivalent_weight(self, molar_mass, stoichiometry_factor):
        return molar_mass * stoichiometry_factor
if __name__ == '__main__':
    calculator = StoichiometryCalculator()
    molar_mass_h2o = 18.015                   
    stoichiometry_factor_h2o = 2.0                                                                             
    equivalent_weight_h2o = calculator.calculate_equivalent_weight(molar_mass_h2o, stoichiometry_factor_h2o)
    print(f"Equivalent weight of H2O: {equivalent_weight_h2o}")