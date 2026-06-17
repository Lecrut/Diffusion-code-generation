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
        if weight2 == 0:
            raise ValueError("Reference weight (weight2) cannot be zero for relative difference calculation.")
        self.validate_inputs(weight1, weight2)
        return abs((weight1 - weight2) / weight2)
    def calculate_percentage_difference(self, weight1, weight2):
        absolute_diff = self.calculate_absolute_difference(weight1, weight2)
        if weight2 == 0:
            raise ValueError("Reference weight (weight2) cannot be zero for percentage difference calculation.")
        return (absolute_diff / abs(weight2)) * 100
def main():
    w_a = 50.0
    w_b = 48.5
    calc = WeightCalculator()
    try:
        absolute_diff = calc.calculate_absolute_difference(w_a, w_b)
        relative_diff = calc.calculate_relative_difference(w_a, w_b)
        percentage_diff = calc.calculate_percentage_difference(w_a, w_b)
        print(f"Absolute Difference: {absolute_diff}")
        print(f"Relative Difference (Decimal): {relative_diff:.6f}")
        print(f"Percentage Difference: {percentage_diff:.2f}%")
    except ValueError as e:
        print(f"Validation Error: {e}")
if __name__ == '__main__':
    main()