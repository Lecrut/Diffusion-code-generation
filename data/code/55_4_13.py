class Triangle:
    def __init__(self, side1, side2, side3):
        self.side1 = side1
        self.side2 = side2
        self.side3 = side3
        if not self.is_valid_triangle():
            raise ValueError("The given side lengths do not form a valid triangle.")

    def is_valid_triangle(self):
        return (self.side1 + self.side2 > self.side3 and
                self.side1 + self.side3 > self.side2 and
                self.side2 + self.side3 > self.side1)

    def perimeter(self):
        return self.side1 + self.side2 + self.side3

if __name__ == '__main__':
    try:
        triangle1 = Triangle(3, 4, 5)
        print(f"Perimeter of (3, 4, 5): {triangle1.perimeter()}")
    except ValueError as e:
        print(f"Error: {e}")

    try:
        triangle2 = Triangle(1, 2, 10)
        print(f"Perimeter of (1, 2, 10): {triangle2.perimeter()}")
    except ValueError as e:
        print(f"Error: {e}")

    try:
        triangle3 = Triangle(5, 5, 5)
        print(f"Perimeter of (5, 5, 5): {triangle3.perimeter()}")
    except ValueError as e:
        print(f"Error: {e}")