import math
class WeightCalculator:
    def validate_inputs(self, weight1, weight2):
        if not isinstance(weight1, (int, float)) or not isinstance(weight2, (int, float)):
            raise ValueError("Both weights must be numeric.")
        if weight1 < 0 or weight2 < 0:
            raise ValueError("Weights cannot be negative.")
    def calculate_absolute_difference(self, weight1, weight2):
        self.validate_inputs(weight1, weight2)
        return abs(weight1 - weight2)
    def calculate_relative_difference(self, weight1, weight2, reference_weight=None):
        if reference_weight is None:
            reference_weight = max(abs(weight1), abs(weight2))
        if reference_weight == 0:
            raise ValueError("Reference weight cannot be zero.")
        self.validate_inputs(weight1, weight2)
        return (abs(weight1 - weight2) / reference_weight) * 100
def main():
    calc = WeightCalculator()
    sample_weights = [5.5, 3.2]
    abs_diff = calc.calculate_absolute_difference(sample_weights[0], sample_weights[1])
    rel_diff = calc.calculate_relative_difference(sample_weights[0], sample_weights[1])
    print(f"Absolute Difference: {abs_diff}")
    print(f"Relative Difference (%): {rel_diff:.2f}%")
if __name__ == '__main__':
    main()