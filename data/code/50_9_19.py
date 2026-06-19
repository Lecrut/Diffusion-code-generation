class AreaCalculator:
    def __init__(self):
        self.valid_types = (int, float)

    def _validate_areas(self, area_a, area_b):
        if not isinstance(area_a, self.valid_types) or not isinstance(area_b, self.valid_types):
            raise ValueError("Both areas must be numbers.")

    def get_difference(self, area_a, area_b):
        self._validate_areas(area_a, area_b)
        return abs(area_a - area_b)

if __name__ == '__main__':
    calculator = AreaCalculator()
    try:
        area1 = 75.2
        area2 = 48.6
        difference = calculator.get_difference(area1, area2)
        print(f"The positive difference is: {difference:.2f}")
    except ValueError as e:
        print(e)