class EquivalentWeightCalculator:
    def __init__(self):
        pass
    def calculate_equivalence(self, substance_a, substance_b, ratio_a, ratio_b):
        if ratio_a == 0 or ratio_b == 0:
            raise ValueError("Ratios cannot be zero")
        weight_a = substance_a * ratio_a
        weight_b = substance_b * ratio_b
        equivalence = (weight_a + weight_b) / (ratio_a + ratio_b)
        return equivalence
if __name__ == '__main__':
    calculator = EquivalentWeightCalculator()
    substance1 = 10.0
    substance2 = 5.0
    ratio1 = 2.0
    ratio2 = 3.0
    try:
        result = calculator.calculate_equivalence(substance1, substance2, ratio1, ratio2)
        print(f"Substance A: {substance1}, Ratio A: {ratio1}")
        print(f"Substance B: {substance2}, Ratio B: {ratio2}")
        print(f"Equivalence calculated: {result}")
    except ValueError as e:
        print(f"Error: {e}")