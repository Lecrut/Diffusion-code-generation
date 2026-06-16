class EquivalentWeightCalculator:
    def __init__(self):
        pass
    def calculate_equivalent_weight(self, substance_a, ratio_a, substance_b, ratio_b):
        if ratio_a == 0 or ratio_b == 0:
            raise ValueError("Ratios cannot be zero")
        weight_a = substance_a * ratio_a
        weight_b = substance_b * ratio_b
        equivalent_weight = weight_a + weight_b
        return equivalent_weight
if __name__ == '__main__':
    calculator = EquivalentWeightCalculator()
    substance1 = 10
    ratio1 = 2.5
    substance2 = 5
    ratio2 = 3.0
    try:
        result = calculator.calculate_equivalent_weight(substance1, ratio1, substance2, ratio2)
        print(result)
    except ValueError as e:
        print(f"Error: {e}")