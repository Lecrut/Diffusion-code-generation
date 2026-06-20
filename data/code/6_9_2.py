class WeightCalculator:
    UNIT_KG = "kg"
    UNIT_LBS = "lbs"
    VALID_UNITS = ("kg", "lbs")

    def __init__(self, weight_a=0.0, weight_b=0.0):
        self._weight_a = float(weight_a)
        self._weight_b = float(weight_b)
        self._difference = 0.0
        self._recalculate()

    def _recalculate(self):
        self._difference = abs(self._weight_a - self._weight_b)

    def set_weight_a(self, value):
        self._weight_a = float(value)
        self._recalculate()

    def set_weight_b(self, value):
        self._weight_b = float(value)
        self._recalculate()

    def get_weight_a(self):
        return self._weight_a

    def get_weight_b(self):
        return self._weight_b

    def get_difference(self):
        return self._difference

    def is_zero_difference(self):
        return self._difference == 0.0

if __name__ == '__main__':
    calc = WeightCalculator(150.5, 120.0)
    diff = calc.get_difference()
    print(diff)
    zero_diff_calc = WeightCalculator(100, 100)
    print(zero_diff_calc.is_zero_difference())
    calc.set_weight_a(200.0)
    print(calc.get_difference())