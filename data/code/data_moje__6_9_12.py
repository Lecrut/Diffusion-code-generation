class WeightCalculator:
    MIN_WEIGHT = 0.0
    MAX_WEIGHT = 1e18
    VALID_TYPES = (int, float)

    def __init__(self, unit_name="kg"):
        if unit_name not in ("kg", "lbs"):
            raise ValueError("Unit must be 'kg' or 'lbs'")
        self.unit_name = unit_name
        self._weight1 = 0.0
        self._weight2 = 0.0

    def set_weight1(self, value):
        self._validate_value(value)
        self._weight1 = float(value)

    def set_weight2(self, value):
        self._validate_value(value)
        self._weight2 = float(value)

    def get_weight1(self):
        return self._weight1

    def get_weight2(self):
        return self._weight2

    def calculate_difference(self):
        return abs(self._weight1 - self._weight2)

    def calculate_signed_difference(self):
        return self._weight1 - self._weight2

    def is_weight1_heavier(self):
        return self._weight1 > self._weight2

    def is_weight2_heavier(self):
        return self._weight2 > self._weight1

    def is_equal(self):
        return self._weight1 == self._weight2

    def _validate_value(self, value):
        if not isinstance(value, self.VALID_TYPES):
            raise TypeError("Weight must be a number")
        if value < self.MIN_WEIGHT or value > self.MAX_WEIGHT:
            raise ValueError("Weight out of valid range")

if __name__ == '__main__':
    calculator = WeightCalculator(unit_name="lbs")
    calculator.set_weight1(200)
    calculator.set_weight2(150)
    abs_diff = calculator.calculate_difference()
    signed_diff = calculator.calculate_signed_difference()
    is_heavier = calculator.is_weight1_heavier()
    print(abs_diff)
    print(signed_diff)
    print(is_heavier)