import sys
class WeightDifferenceCalculator:
    def validate_inputs(self, weight1: float, weight2: float) -> bool:
        if not isinstance(weight1, (int, float)) or not isinstance(weight2, (int, float)):
            return False
        if weight1 < 0 or weight2 < 0:
            return False
        try:
            abs_weight1 = abs(float(weight1))
            abs_weight2 = abs(float(weight2))
        except ValueError:
            return False
        return True
    def calculate_absolute_difference(self, w_a: float, w_b: float) -> float:
        if not self.validate_inputs(w_a, w_b):
            raise ValueError("Input validation failed. Weights must be non-negative numbers.")
        result = abs(float(w_a)) - abs(float(w_b))
        return round(result, 2)
    def calculate_relative_difference(self, base_weight: float, target_weight: float) -> float:
        if not self.validate_inputs(base_weight, target_weight):
            raise ValueError("Input validation failed. Base weight must be a non-negative number.")
        try:
            diff = abs(float(target_weight)) - abs(float(base_weight))
            rel_diff = (diff / abs(float(base_weight))) * 100 if abs(float(base_weight)) != 0 else float('inf')
        except ZeroDivisionError:
            return None
        return round(rel_diff, 2)
def main():
    calc = WeightDifferenceCalculator()
    weight_a = 50.5
    weight_b = 48.3
    abs_diff = calc.calculate_absolute_difference(weight_a, weight_b)
    rel_diff = calc.calculate_relative_difference(weight_a, weight_b)
    print(f"Absolute Difference: {abs_diff}")
    if rel_diff is not None:
        print(f"Relative Difference (%): {rel_diff}%")
if __name__ == '__main__':
    main()