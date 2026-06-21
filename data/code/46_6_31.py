class Triangle:
    def __init__(self, side_a, side_b, side_c):
        self._validate_sides(side_a, side_b, side_c)
        self.side_a = side_a
        self.side_b = side_b
        self.side_c = side_c

    def _validate_sides(self, side_a, side_b, side_c):
        if not all(isinstance(x, (int, float)) and x > 0 for x in [side_a, side_b, side_c]):
            raise ValueError("All sides must be positive numbers.")
        if not (side_a + side_b > side_c and side_a + side_c > side_b and side_b + side_c > side_a):
            raise ValueError("The given sides do not form a valid triangle.")

    def perimeter(self):
        return self.side_a + self.side_b + self.side_c

if __name__ == '__main__':
    try:
        triangle = Triangle(10, 24, 26)
        print(f"Perimeter: {triangle.perimeter()}")
        print(f"Side A: {triangle.side_a}, Side B: {triangle.side_b}, Side C: {triangle.side_c}")
    except ValueError as e:
        print(e)