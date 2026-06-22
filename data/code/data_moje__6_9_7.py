class WeightCalculator:
    MIN_WEIGHT = 0.0

    def __init__(self, weight_one, weight_two):
        self._weight_one = float(weight_one)
        self._weight_two = float(weight_two)

    def _validate_weight(self, weight_value):
        if weight_value < self.MIN_WEIGHT:
            raise ValueError("Weight must be non-negative")
        return weight_value

    def get_weight_one(self):
        return self._weight_one

    def get_weight_two(self):
        return self._weight_two

    def set_weight_one(self, new_weight):
        self._weight_one = self._validate_weight(new_weight)

    def set_weight_two(self, new_weight):
        self._weight_two = self._validate_weight(new_weight)

    def calculate_difference(self):
        val_one = self._weight_one
        val_two = self._weight_two
        raw_diff = val_one - val_two
        if raw_diff < 0:
            return -raw_diff
        return raw_diff

if __name__ == '__main__':
    calc = WeightCalculator(85.5, 72.3)
    diff = calc.calculate_difference()
    print(diff)
    calc.set_weight_one(90.0)
    new_diff = calc.calculate_difference()
    print(new_diff)