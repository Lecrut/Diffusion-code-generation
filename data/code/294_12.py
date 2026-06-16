class StoichiometryCalculator:
    def calculate_equivalent_weight(self, molar_mass, stoichiometry_factor):
        return molar_mass * stoichiometry_factor
if __name__ == '__main__':
    calculator = StoichiometryCalculator()
    molar_mass_substance = 100.0
    stoichiometry_factor_reaction = 2.5
    equivalent_weight = calculator.calculate_equivalent_weight(molar_mass_substance, stoichiometry_factor_reaction)
    print(f"Molar Mass of Substance: {molar_mass_substance}")
    print(f"Stoichiometry Factor: {stoichiometry_factor_reaction}")
    print(f"Equivalent Weight: {equivalent_weight}")