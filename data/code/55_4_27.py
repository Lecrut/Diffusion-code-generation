class Triangle:
    MINIMUM_SIDE_LENGTH = 1

    def __init__(self, side1, side2, side3):
        if not self.is_valid(side1, side2, side3):
            raise ValueError("The given side lengths do not form a valid triangle.")
        self.side1 = side1
        self.side2 = side2
        self.side3 = side3

    @staticmethod
    def is_valid(a, b, c):
        return (a >= Triangle.MINIMUM_SIDE_LENGTH and
                b >= Triangle.MINIMUM_SIDE_LENGTH and
                c >= Triangle.MINIMUM_SIDE_LENGTH and
                a + b > c and
                a + c > b and
                b + c > a)

    def perimeter(self):
        return self.side1 + self.side2 + self.side3

if __name__ == '__main__':
    try:
        triangle1 = Triangle(7, 8, 9)
        print(f"Perimeter of (7, 8, 9): {triangle1.perimeter()}")
    except ValueError as e:
        print(f"Error: {e}")

    try:
        triangle2 = Triangle(10, 15, 25)
        print(f"Perimeter of (10, 15, 25): {triangle2.perimeter()}")
    except ValueError as e:
        print(f"Error: {e}")