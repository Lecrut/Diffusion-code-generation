import math
class WeightCalculator:
    def calculate_difference(self, weight_a: float, weight_b: float) -> float:
        return abs(weight_a - weight_b)
    def normalize_weight(self, raw_value: float, max_capacity: float = 100.0) -> float:
        if max_capacity <= 0:
            raise ValueError("Max capacity must be positive.")
        return min(raw_value / max_capacity, 1.0)
    def adjust_weight(self, current_weight: float, adjustment_factor: float = 1.5) -> float:
        if not isinstance(adjustment_factor, (int, float)):
            raise TypeError("Adjustment factor must be numeric.")
        return round(current_weight * adjustment_factor, 2)
if __name__ == '__main__':
    calculator = WeightCalculator()
    sample_weights = [50.0, 75.5]
    max_capacity = 100.0
    diff_result = calculator.calculate_difference(sample_weights[0], sample_weights[1])
    normalized_a = calculator.normalize_weight(80.0)
    adjusted_b = calculator.adjust_weight(45.0, adjustment_factor=2.0)
    print(f"Difference: {diff_result}")
    print(f"Normalized A: {normalized_a}")
    print(f"Adjusted B: {adjusted_b}")