class EquivalentWeightCalculator:
    def __init__(self):
        pass
    def calculate_equivalent_weight(self, mass, stoichiometry_ratios):
        total_equivalent_weight = 0.0
        for substance, ratio in stoichiometry_ratios.items():
            if substance in mass:
                mass_of_substance = mass[substance]
                equivalent_weight = mass_of_substance * ratio
                total_equivalent_weight += equivalent_weight
            else:
                print(f"Warning: Substance {substance} not found in input mass.")
        return total_equivalent_weight
if __name__ == '__main__':
    calculator = EquivalentWeightCalculator()
    sample_mass = {
        "H2O": 18.015,
        "NaCl": 58.44,
        "Fe": 55.845
    }
    sample_ratios = {
        "H2O": 1.0,
        "NaCl": 1.1,
        "Fe": 0.95
    }
    result = calculator.calculate_equivalent_weight(sample_mass, sample_ratios)
    print(f"Sample Mass Data: {sample_mass}")
    print(f"Stoichiometry Ratios: {sample_ratios}")
    print(f"Calculated Equivalent Weight: {result}")