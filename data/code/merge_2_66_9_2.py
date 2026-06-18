import math
class WeightCalculator:
    def validate_inputs(self, weight1, weight2):
        if not isinstance(weight1, (int, float)) or not isinstance(weight2, (int, float)):
            raise TypeError("Both weights must be numeric values.")
        if weight1 < 0 or weight2 < 0:
            raise ValueError("Weights cannot be negative.")
    def calculate_absolute_difference(self, weight1, weight2):
        self.validate_inputs(weight1, weight2)
        return abs(weight1 - weight2)
    def calculate_relative_difference(self, weight1, weight2):
        if not (isinstance(weight1, (int, float)) and isinstance(weight2, (int, float))) or weight1 < 0:
            raise ValueError("Relative difference requires positive numeric values.")
        return abs((weight1 - weight2) / weight2)
def main():
    calc = WeightCalculator()
    sample_weight_a = 50.0
    sample_weight_b = 75.0
    absolute_diff = calc.calculate_absolute_difference(sample_weight_a, sample_weight_b)
    relative_diff = calc.calculate_relative_difference(sample_weight_a, sample_weight_b)
    print(f"Absolute Difference: {absolute_diff}")
    print(f"Relative Difference (based on weight A): {relative_diff:.4f}")
if __name__ == '__main__':
    main()