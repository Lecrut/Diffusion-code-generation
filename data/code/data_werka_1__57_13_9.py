class TriangleArea:
    def __init__(self, base, height):
        self.base = base
        self.height = height
        self._validate_dimensions()

    def _validate_dimensions(self):
        if self.base <= 0 or self.height <= 0:
            raise ValueError("Base and height must be positive numbers.")

    def compute_area(self):
        return 0.5 * self.base * self.height

if __name__ == '__main__':
    base_value = 6
    height_value = 8
    try:
        triangle_area_calculator = TriangleArea(base_value, height_value)
        area_result = triangle_area_calculator.compute_area()
        print(area_result)
    except ValueError as e:
        print(e)