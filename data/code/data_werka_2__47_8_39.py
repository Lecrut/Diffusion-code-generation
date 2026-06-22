class Triangle:
    BASE_MULTIPLIER = 0.5

    def __init__(self, base, height):
        if not self._is_valid_dimension(base) or not self._is_valid_dimension(height):
            raise ValueError("Base and height must be positive numbers.")
        self.base = base
        self.height = height

    def area(self):
        return self.BASE_MULTIPLIER * self.base * self.height

    @staticmethod
    def _is_valid_dimension(dimension):
        return dimension > 0

if __name__ == '__main__':
    triangle = Triangle(15, 4)
    print(f"The area of the triangle is: {triangle.area()}")