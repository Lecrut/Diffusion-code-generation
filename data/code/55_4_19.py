class Triangle:
    def __init__(self, side1, side2, side3):
        self.side1 = side1
        self.side2 = side2
        self.side3 = side3

    @staticmethod
    def is_valid_triangle(a, b, c):
        return a + b > c and a + c > b and b + c > a

    def calculate_perimeter(self):
        if not Triangle.is_valid_triangle(self.side1, self.side2, self.side3):
            raise ValueError("The given side lengths do not form a valid triangle.")
        return self.side1 + self.side2 + self.side3

if __name__ == '__main__':
    try:
        triangle1 = Triangle(3, 4, 5)
        print(f"Perimeter of (3, 4, 5): {triangle1.calculate_perimeter()}")
    except ValueError as e:
        print(f"Error: {e}")

    try:
        triangle2 = Triangle(1, 2, 10)
        print(f"Perimeter of (1, 2, 10): {triangle2.calculate_perimeter()}")
    except ValueError as e:
        print(f"Error: {e}")

    try:
        triangle3 = Triangle(5, 5, 5)
        print(f"Perimeter of (5, 5, 5): {triangle3.calculate_perimeter()}")
    except ValueError as e:
        print(f"Error: {e}")