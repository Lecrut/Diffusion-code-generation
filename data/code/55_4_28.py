class Triangle:
    MIN_SIDE_LENGTH = 1

    def __init__(self, side1, side2, side3):
        if not self.is_valid_triangle(side1, side2, side3):
            raise ValueError("The given side lengths do not form a valid triangle.")
        self.side1 = side1
        self.side2 = side2
        self.side3 = side3

    def is_valid_triangle(self, a, b, c):
        return (a >= Triangle.MIN_SIDE_LENGTH and
                b >= Triangle.MIN_SIDE_LENGTH and
                c >= Triangle.MIN_SIDE_LENGTH and
                a + b > c and
                a + c > b and
                b + c > a)

    def perimeter(self):
        return self.side1 + self.side2 + self.side3

if __name__ == '__main__':
    try:
        triangle = Triangle(7, 10, 5)
        print(f"Perimeter of (7, 10, 5): {triangle.perimeter()}")
    except ValueError as e:
        print(f"Error: {e}")

    try:
        invalid_triangle = Triangle(1, 2, 3)
        print(f"Perimeter of (1, 2, 3): {invalid_triangle.perimeter()}")
    except ValueError as e:
        print(f"Error: {e}")