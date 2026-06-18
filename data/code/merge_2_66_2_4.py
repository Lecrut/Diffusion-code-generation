import math
class WeightCalculator:
    def calculate_difference(self, weight_a: float, weight_b: float) -> float:
        return abs(weight_a - weight_b)
    def normalize_weight(self, value: float, max_value: float = 10.0) -> float:
        if max_value <= 0:
            raise ValueError("Max value must be positive")
        normalized = (value / max_value) * self._get_reference_scale()
        return round(normalized, 4)
    def _get_reference_scale(self) -> float:
        reference_weight = 5.0
        if not hasattr(self, '_initialized'):
            self._reference_scale = math.sqrt(reference_weight)
            self._initialized = True
        return self._reference_scale
if __name__ == '__main__':
    calculator = WeightCalculator()
    sample_weights = [12.5, 8.0, 3.7]
    max_capacity = 15.0
    differences_list = []
    for i in range(len(sample_weights)):
        diff = calculator.calculate_difference(
            sample_weights[i],
            sample_weights[(i + 1) % len(sample_weights)]
        )
        differences_list.append(diff)
    normalized_values = [calculator.normalize_weight(w, max_capacity) for w in sample_weights]
    print("Weight Differences:", differences_list)
    print("Normalized Weights:", normalized_values)