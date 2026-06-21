class AreaCalculator:
    def get_difference(self, area_a, area_b):
        self._validate_area(area_a)
        self._validate_area(area_b)
        return abs(area_a - area_b)

    def _validate_area(self, area):
        if not isinstance(area, (int, float)):
            raise ValueError("Area must be a number")

if __name__ == '__main__':
    calculator = AreaCalculator()
    area1 = 75.0
    area2 = 40.0
    difference = calculator.get_difference(area1, area2)
    print(difference)