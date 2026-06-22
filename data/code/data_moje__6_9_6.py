class WeightCalculator:
    def __init__(self, initial_weight_a=0.0, initial_weight_b=0.0):
        self._weight_a = float(initial_weight_a)
        self._weight_b = float(initial_weight_b)
        self._last_difference = 0.0
        self._recalculate()

    def _recalculate(self):
        self._last_difference = abs(self._weight_a - self._weight_b)
        return self._last_difference

    def set_weight_a(self, new_value):
        if new_value < 0:
            raise ValueError("Weight A cannot be negative")
        self._weight_a = float(new_value)
        return self._recalculate()

    def set_weight_b(self, new_value):
        if new_value < 0:
            raise ValueError("Weight B cannot be negative")
        self._weight_b = float(new_value)
        return self._recalculate()

    def get_difference(self):
        return self._last_difference

    def get_weights(self):
        return self._weight_a, self._weight_b

    def update_weights(self, weight_a, weight_b):
        self.set_weight_a(weight_a)
        self.set_weight_b(weight_b)
        return self._last_difference

if __name__ == '__main__':
    w1 = 250.75
    w2 = 180.25
    calc = WeightCalculator(w1, w2)
    diff = calc.get_difference()
    print(diff)
    new_w1 = 300.0
    new_w2 = 300.0
    updated_diff = calc.update_weights(new_w1, new_w2)
    print(updated_diff)
    current_a, current_b = calc.get_weights()
    print(current_a)
    print(current_b)