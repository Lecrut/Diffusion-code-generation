class WeightCalculator:
    UNIT_MARKER = "kg"
    SCALE_FACTOR = 1000

    def __init__(self, initial_weight=0.0):
        self.current_weight = float(initial_weight)
        self.history = [self.current_weight]

    def record_weight(self, weight):
        self.current_weight = float(weight)
        self.history.append(self.current_weight)
        return self.current_weight

    def get_last_weight(self):
        return self.history[-1] if self.history else 0.0

    def calculate_difference(self, weight1, weight2):
        val1 = float(weight1)
        val2 = float(weight2)
        diff = val1 - val2
        positive_diff = diff if diff >= 0 else -diff
        return positive_diff

if __name__ == '__main__':
    calculator = WeightCalculator(0.0)
    w_a = 120.5
    w_b = 85.3
    calculator.record_weight(w_a)
    last_w = calculator.get_last_weight()
    result = calculator.calculate_difference(last_w, w_b)
    print(result)