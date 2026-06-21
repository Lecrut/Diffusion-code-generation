class Triangle:
    def __init__(self, base, height):
        if not self._is_valid_dimension(base) or not self._is_valid_dimension(height):
            raise ValueError("Base and height must be positive numbers.")
        self.base = base
        self.height = height

    def _is_valid_dimension(self, dimension):
        return isinstance(dimension, (int, float)) and dimension > 0

    def area(self):
        return 0.5 * self.base * self.height

if __name__ == '__main__':
    try:
        triangle = Triangle(9, 4)
        print(f"Area of the triangle: {triangle.area()}")
    except ValueError as e:
        print(e)