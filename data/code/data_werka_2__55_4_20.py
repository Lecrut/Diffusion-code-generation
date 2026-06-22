class Triangle:
    MIN_SIDE_LENGTH = 1

    def __init__(self, side1, side2, side3):
        if not (side1 >= self.MIN_SIDE_LENGTH and side2 >= self.MIN_SIDE_LENGTH and side3 >= self.MIN_SIDE_LENGTH):
            raise ValueError("Side lengths must be greater than or equal to the minimum side length.")
        if not (side1 + side2 > side3 and side1 + side3 > side2 and side2 + side3 > side1):
            raise ValueError("The given side lengths do not form a valid triangle.")
        self.side1 = side1
        self.side2 = side2
        self.side3 = side3

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