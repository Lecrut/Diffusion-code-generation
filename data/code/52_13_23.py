class Triangle:
    def __init__(self, base, height):
        self.base = base
        self.height = height
        self._validate_inputs()

    def _validate_inputs(self):
        if self.base <= 0 or self.height <= 0:
            raise ValueError("Base and height must be positive numbers.")

    def calculate_area(self):
        return 0.5 * self.base * self.height

if __name__ == '__main__':
    base = 15
    height = 7
    triangle = Triangle(base, height)
    area = triangle.calculate_area()
    print(area)