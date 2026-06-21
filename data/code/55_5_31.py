class Triangle:
    def __init__(self, side1, side2, side3):
        self.sides = [side1, side2, side3]
        self.validate_sides()

    def validate_sides(self):
        a, b, c = sorted(self.sides)
        if not (a + b > c):
            raise ValueError("Invalid triangle sides")

    def perimeter(self):
        return sum(self.sides)

if __name__ == '__main__':
    try:
        triangle = Triangle(6, 8, 10)
        print(f"Perimeter: {triangle.perimeter()}")
        print(f"Sides: {triangle.sides}")
    except ValueError as e:
        print(e)