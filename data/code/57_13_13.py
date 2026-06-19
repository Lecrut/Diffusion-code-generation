class TriangleCalculator:
    def __init__(self, base, height):
        self.base = base
        self.height = height
        self._validate_dimensions()

    def _validate_dimensions(self):
        if not isinstance(self.base, (int, float)) or not isinstance(self.height, (int, float)):
            raise TypeError("Base and height must be numbers.")
        if self.base <= 0 or self.height <= 0:
            raise ValueError("Base and height must be positive numbers.")

    def calculate_area(self):
        return 0.5 * self.base * self.height

if __name__ == '__main__':
    base_value = 6
    height_value = 8
    try:
        calculator = TriangleCalculator(base_value, height_value)
        area_result = calculator.calculate_area()
        print(area_result)
    except (TypeError, ValueError) as e:
        print(e)