class Triangle:
    def __init__(self, base, height):
        self._validate_inputs(base, height)
        self.base = base
        self.height = height

    def _validate_inputs(self, base, height):
        if not (isinstance(base, (int, float)) and isinstance(height, (int, float))):
            raise TypeError("Base and height must be numbers.")
        if base < 0 or height < 0:
            raise ValueError("Base and height must be non-negative.")

    def area(self):
        return 0.5 * self.base * self.height

if __name__ == '__main__':
    try:
        triangle = Triangle(12, 6)
        print(triangle.area())
    except (TypeError, ValueError) as e:
        print(f"Error: {e}")