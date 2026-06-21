class Triangle:
    def __init__(self, side_a, side_b, side_c):
        self._validate_sides(side_a, side_b, side_c)
        self.side_a = side_a
        self.side_b = side_b
        self.side_c = side_c

    def _validate_sides(self, a, b, c):
        if not all(isinstance(x, (int, float)) and x > 0 for x in [a, b, c]):
            raise ValueError("All sides must be positive numbers.")
        if not (a + b > c and a + c > b and b + c > a):
            raise ValueError("The given sides do not form a valid triangle.")

    def perimeter(self):
        return self.side_a + self.side_b + self.side_c

if __name__ == '__main__':
    try:
        triangle = Triangle(10, 6, 8)
        print(f"Perimeter: {triangle.perimeter()}")
        print(f"Sides: a={triangle.side_a}, b={triangle.side_b}, c={triangle.side_c}")
    except ValueError as e:
        print(e)