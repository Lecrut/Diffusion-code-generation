class Triangle:
    def __init__(self, side_a, side_b, side_c):
        if not all(isinstance(side, (int, float)) for side in [side_a, side_b, side_c]):
            raise ValueError("All sides must be numbers.")
        if any(side <= 0 for side in [side_a, side_b, side_c]):
            raise ValueError("All sides must be positive numbers.")
        if not self.is_valid_triangle(side_a, side_b, side_c):
            raise ValueError("The given sides do not form a valid triangle.")
        self.side_a = side_a
        self.side_b = side_b
        self.side_c = side_c

    def is_valid_triangle(self, side_a, side_b, side_c):
        return (side_a + side_b > side_c and
                side_a + side_c > side_b and
                side_b + side_c > side_a)

    def perimeter(self):
        return self.side_a + self.side_b + self.side_c

if __name__ == '__main__':
    try:
        triangle = Triangle(10, 6, 8)
        print(f"Perimeter: {triangle.perimeter()}")
    except ValueError as e:
        print(e)