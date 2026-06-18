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
    def calculate_relative_difference(self, weight1, reference_weight):
        if not isinstance(reference_weight, (int, float)):
            raise TypeError("Reference weight must be numeric.")
        if reference_weight <= 0:
            raise ValueError("Reference weight for relative difference cannot be zero or negative.")
        self.validate_inputs(weight1, reference_weight)
        return abs((weight1 - reference_weight) / reference_weight)
def main():
    calculator = WeightCalculator()
    sample_weights = [5.2, 4.8]
    reference_weight = 5.0
    try:
        absolute_diff = calculator.calculate_absolute_difference(sample_weights[0], sample_weights[1])
        relative_diff_1 = calculator.calculate_relative_difference(sample_weights[0], reference_weight)
        relative_diff_2 = calculator.calculate_relative_difference(sample_weights[1], reference_weight)
        print(f"Absolute Difference: {absolute_diff}")
        print(f"Relative Difference (Weight 1 vs Reference): {relative_diff_1:.4f}")
        print(f"Relative Difference (Weight 2 vs Reference): {relative_diff_2:.4f}")
    except Exception as e:
        print(f"Error during calculation: {e}")
if __name__ == '__main__':
    main()