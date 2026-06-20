class WeightCalculator:
    _MIN_WEIGHT = 0.0

    def __init__(self, tolerance=1e-9):
        self.tolerance = float(tolerance)

    def calculate_difference(self, weight1, weight2):
        w1 = float(weight1)
        w2 = float(weight2)
        if w1 < self._MIN_WEIGHT:
            raise ValueError("Weight1 cannot be negative")
        if w2 < self._MIN_WEIGHT:
            raise ValueError("Weight2 cannot be negative")
        diff = abs(w1 - w2)
        if diff < self.tolerance:
            return 0.0
        return diff

if __name__ == '__main__':
    calculator = WeightCalculator()
    weight_a = 75.5
    weight_b = 75.5000000001
    difference = calculator.calculate_difference(weight_a, weight_b)
    print(difference)