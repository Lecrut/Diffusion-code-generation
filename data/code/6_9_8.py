class WeightCalculator:
    def __init__(self):
        self._history = []

    def calculate_difference(self, weight1, weight2):
        if not isinstance(weight1, (int, float)) or not isinstance(weight2, (int, float)):
            raise TypeError("Weights must be numeric")
        if weight1 < 0 or weight2 < 0:
            raise ValueError("Weights cannot be negative")
        difference = abs(weight1 - weight2)
        self._history.append((weight1, weight2, difference))
        return difference

    def get_history(self):
        return list(self._history)

    def clear_history(self):
        self._history = []

if __name__ == '__main__':
    calculator = WeightCalculator()
    sample_weight_one = 85.75
    sample_weight_two = 110.25
    diff_result = calculator.calculate_difference(sample_weight_one, sample_weight_two)
    print(diff_result)
    print(calculator.calculate_difference(50.0, 50.0))