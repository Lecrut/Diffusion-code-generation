class TriangleCalculator:
    def __init__(self, base, height):
        self.base = base
        self.height = height
        if not (isinstance(base, (int, float)) and isinstance(height, (int, float))):
            raise TypeError("Base and height must be numbers.")
        if base <= 0 or height <= 0:
            raise ValueError("Base and height must be positive numbers.")

    def compute_area(self):
        return 0.5 * self.base * self.height

if __name__ == '__main__':
    try:
        base_value = 6
        height_value = 8
        calculator = TriangleCalculator(base_value, height_value)
        area_result = calculator.compute_area()
        print(area_result)
    except (TypeError, ValueError) as e:
        print(e)