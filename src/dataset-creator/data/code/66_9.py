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
        self.validate_inputs(weight1, weight2)
        if weight2 == 0:
            raise ZeroDivisionError("Reference weight cannot be zero for relative difference calculation.")
        return (weight1 - weight2) / abs(weight2)
def main():
    calculator = WeightCalculator()
    sample_weight_older_unit = 5.5
    sample_weight_newer_unit = 6.0
    absolute_diff = calculator.calculate_absolute_difference(sample_weight_older_unit, sample_weight_newer_unit)
    relative_diff = calculator.calculate_relative_difference(sample_weight_older_unit, sample_weight_newer_unit)
    print(f"Absolute Difference: {absolute_diff}")
    print(f"Relative Difference (Old vs New): {relative_diff:.4f}")
if __name__ == '__main__':
    main()