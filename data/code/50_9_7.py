class AreaCalculator:
    def get_difference(self, area_a, area_b):
        self._validate_area(area_a)
        self._validate_area(area_b)
        return abs(area_a - area_b)

    def _validate_area(self, area):
        if not isinstance(area, (int, float)):
            raise ValueError("Area must be a number.")

if __name__ == '__main__':
    calculator = AreaCalculator()
    try:
        area1 = 100.5
        area2 = 45.3
        difference = calculator.get_difference(area1, area2)
        print(f"The positive difference is: {difference:.2f}")
    except ValueError as e:
        print(e)