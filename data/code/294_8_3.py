class EquivalentWeightCalculator:
    def __init__(self):
        pass
    def calculate_equivalent_weight(self, mass_A, ratio_A, mass_B, ratio_B):
        if ratio_A == 0 or ratio_B == 0:
            raise ValueError("Ratios cannot be zero")
        weight_A = mass_A * ratio_A
        weight_B = mass_B * ratio_B
        total_equivalent_weight = weight_A + weight_B
        return total_equivalent_weight
if __name__ == '__main__':
    calculator = EquivalentWeightCalculator()
    mass_a = 10.0
    ratio_a = 2.5
    mass_b = 15.0
    ratio_b = 1.8
    try:
        result = calculator.calculate_equivalent_weight(mass_a, ratio_a, mass_b, ratio_b)
        print(result)
    except ValueError as e:
        print(f"Error: {e}")