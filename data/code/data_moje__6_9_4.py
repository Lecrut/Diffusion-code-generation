MAX_WEIGHT = 1000000.0

class WeightCalculator:
    def __init__(self):
        self._history = []

    def _validate_weight(self, weight):
        if not isinstance(weight, (int, float)):
            raise TypeError("Weight must be a number")
        if weight < 0:
            raise ValueError("Weight cannot be negative")
        if weight > MAX_WEIGHT:
            raise ValueError("Weight exceeds maximum limit")
        return float(weight)

    def calculate_difference(self, weight1, weight2):
        w1 = self._validate_weight(weight1)
        w2 = self._validate_weight(weight2)
        diff = abs(w1 - w2)
        self._history.append(diff)
        return diff

    def get_last_calculation(self):
        return self._history[-1] if self._history else 0.0

    def get_history(self):
        return list(self._history)

if __name__ == '__main__':
    calc = WeightCalculator()
    first_diff = calc.calculate_difference(150.5, 120.0)
    print(first_diff)
    second_diff = calc.calculate_difference(200.0, 195.0)
    print(second_diff)
    print(calc.get_last_calculation())
    print(calc.get_history())