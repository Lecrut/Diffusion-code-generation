class Triangle:
    def __init__(self, base, height):
        self.base = base
        self.height = height
        if not self._validate_dimensions():
            raise ValueError("Base and height must be positive numbers.")

    def _validate_dimensions(self):
        return self.base > 0 and self.height > 0

    def area(self):
        return 0.5 * self.base * self.height

if __name__ == '__main__':
    try:
        triangle = Triangle(9, 4)
        print(f"Area of the triangle: {triangle.area()}")
    except ValueError as e:
        print(e)