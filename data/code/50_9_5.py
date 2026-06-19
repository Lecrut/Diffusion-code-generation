class AreaCalculator:
    def get_difference(self, area_a, area_b):
        self._validate_areas(area_a, area_b)
        return abs(area_a - area_b)

    def _validate_areas(self, area_a, area_b):
        if not isinstance(area_a, (int, float)):
            raise ValueError(f"Area A must be a number, got {type(area_a).__name__}.")
        if not isinstance(area_b, (int, float)):
            raise ValueError(f"Area B must be a number, got {type(area_b).__name__}.")

if __name__ == '__main__':
    calculator = AreaCalculator()
    area1 = 75.2
    area2 = 48.9
    try:
        difference = calculator.get_difference(area1, area2)
        print(f"The positive difference is: {difference:.2f}")
    except ValueError as e:
        print(e)