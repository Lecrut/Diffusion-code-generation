class WeightCalculator:
    VALID_UNITS = ('kg', 'lbs', 'g')

    def __init__(self, weight1, weight2, unit='kg'):
        self._weight1 = self._validate_weight(weight1)
        self._weight2 = self._validate_weight(weight2)
        self._unit = self._validate_unit(unit)
        self._difference = self._compute_difference()

    def _validate_weight(self, value):
        if value is None:
            raise ValueError("Weight cannot be None")
        numeric_value = float(value)
        if numeric_value < 0:
            raise ValueError("Weight cannot be negative")
        return numeric_value

    def _validate_unit(self, unit):
        if unit is None:
            return 'kg'
        if unit not in self.VALID_UNITS:
            raise ValueError(f"Invalid unit: {unit}")
        return unit

    def _compute_difference(self):
        return abs(self._weight1 - self._weight2)

    def get_difference(self):
        return self._difference

    def get_unit(self):
        return self._unit

    def set_weight1(self, new_weight):
        self._weight1 = self._validate_weight(new_weight)
        self._difference = self._compute_difference()
        return self._difference

    def set_weight2(self, new_weight):
        self._weight2 = self._validate_weight(new_weight)
        self._difference = self._compute_difference()
        return self._difference

if __name__ == '__main__':
    calculator = WeightCalculator(150.5, 120.0, 'kg')
    result = calculator.get_difference()
    print(result)
    updated_weight = calculator.set_weight1(160.0)
    print(updated_weight)
    unit = calculator.get_unit()
    print(unit)