class EquivalentWeightCalculator:
    MOLEAR_MASS_BACL2 = 207.2
    ATOMIC_MASS_CL = 35.45
    
    @staticmethod
    def calculate_equivalent_weight(mass_bacl2):
        equivalent_weight = mass_bacl2 / (EquivalentWeightCalculator.MOLEAR_MASS_BACL2 - 2 * EquivalentWeightCalculator.ATOMIC_MASS_CL)
        return equivalent_weight

if __name__ == '__main__':
    sample_mass_bacl2 = 207
    result = EquivalentWeightCalculator.calculate_equivalent_weight(sample_mass_bacl2)
    print(result)