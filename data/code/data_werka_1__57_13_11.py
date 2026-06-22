class Triangle:
    def __init__(self, base, height):
        self.base = base
        self.height = height
        self._validate_dimensions()

    def _validate_dimensions(self):
        if self.base <= 0 or self.height <= 0:
            raise ValueError("Base and height must be positive numbers.")

    def area(self):
        return 0.5 * self.base * self.height

if __name__ == '__main__':
    try:
        base = 6
        height = 8
        triangle = Triangle(base, height)
        print(triangle.area())
    except ValueError as e:
        print(e)