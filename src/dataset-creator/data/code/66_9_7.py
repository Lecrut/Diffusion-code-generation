import math
class WeightCalculator:
    def validate_inputs(self, weight1, weight2):
        if not isinstance(weight1, (int, float)) or not isinstance(weight2, (int, float)):
            raise ValueError("Both weights must be numeric values.")
        if weight1 < 0 or weight2 < 0:
            raise ValueError("Weights cannot be negative.")
    def calculate_absolute_difference(self, weight1, weight2):
        self.validate_inputs(weight1, weight2)
        return abs(weight1 - weight2)
    def calculate_relative_difference(self, weight1, weight2):
        if not isinstance(weight1, (int, float)) or not isinstance(weight2, (int, float)):
            raise ValueError("Both weights must be numeric values.")
        if weight2 == 0:
            return None
        relative_diff = abs(weight1 - weight2) / abs(weight2)
        return round(relative_diff * 100, 4)
    def calculate_both(self, weight1, weight2):
        self.validate_inputs(weight1, weight2)
        absolute_diff = abs(weight1 - weight2)
        relative_diff = None if weight2 == 0 else (abs(weight1 - weight2) / abs(weight2)) * 100
        return {
            "absolute_difference": round(absolute_diff, 4),
            "relative_difference_percentage": round(relative_diff, 4) if relative_diff is not None else float("inf")
        }
if __name__ == '__main__':
    calculator = WeightCalculator()
    sample_weight1 = 50.75
    sample_weight2 = 63.2
    result_both = calculator.calculate_both(sample_weight1, sample_weight2)
    print("Absolute Difference:", result_both["absolute_difference"])
    print("Relative Difference (%):", result_both["relative_difference_percentage"])