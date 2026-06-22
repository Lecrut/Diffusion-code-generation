class ChemicalCalculator:
    def __init__(self, molecular_weight):
        self.molecular_weight = molecular_weight

    def calculate_equivalent_weight(self, mass):
        return mass * (self.molecular_weight / 100.0)

if __name__ == '__main__':
    calculator = ChemicalCalculator(molecular_weight=44.01)
    equivalent_weight = calculator.calculate_equivalent_weight(44)
    print(equivalent_weight)