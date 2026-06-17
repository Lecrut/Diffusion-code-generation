import math
class WeightDifferenceCalculator:
    def validate_inputs(self, weight1: float, weight2: float) -> bool:
        if not isinstance(weight1, (int, float)) or not isinstance(weight2, (int, float)):
            return False
        if math.isnan(weight1) or math.isnan(weight2):
            return False
        if math.isinf(weight1) or math.isinf(weight2):
            return False
        return True
    def calculate_absolute_difference(self, weight1: float, weight2: float) -> float:
        abs_diff = abs(weight1 - weight2)
        return round(abs_diff, 4)
    def calculate_relative_difference(self, weight1: float, weight2: float) -> float:
        if self.validate_inputs(weight1, weight2):
            reference_weight = max(weight1, weight2)
            rel_diff = abs((weight1 - weight2) / reference_weight) * 100
            return round(rel_diff, 4)
        else:
            raise ValueError("Input validation failed.")
def main():
    calculator = WeightDifferenceCalculator()
    sample_weights = [75.5, 80.2]
    if not calculator.validate_inputs(sample_weights[0], sample_weights[1]):
        print("Error: Invalid inputs provided.")
        return
    abs_diff_result = calculator.calculate_absolute_difference(sample_weights[0], sample_weights[1])
    rel_diff_result = calculator.calculate_relative_difference(sample_weights[0], sample_weights[1])
    print(f"Absolute Difference: {abs_diff_result}")
    print(f"Relative Difference (percentage): {rel_diff_result}%")
if __name__ == '__main__':
    main()