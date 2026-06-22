class CO2EquivalentCalculator:
    MOLECULAR_WEIGHT = 44.01

    @staticmethod
    def calculate_equivalent_weight(mass):
        if CO2EquivalentCalculator.MOLECULAR_WEIGHT == 0:
            return float('inf')
        return mass * (CO2EquivalentCalculator.MOLECULAR_WEIGHT / 100)
if __name__ == '__main__':
    calculator = CO2EquivalentCalculator()
    equivalent_weight = calculator.calculate_equivalent_weight(44)
    print(equivalent_weight)