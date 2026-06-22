class Triangle:
    def __init__(self, side1, side2, side3):
        self.sides = [side1, side2, side3]
        self.validate_sides()

    def validate_sides(self):
        for i in range(3):
            if not (self.sides[i] + self.sides[(i + 1) % 3] > self.sides[(i + 2) % 3]):
                raise ValueError("Invalid triangle sides")

    def perimeter(self):
        return sum(self.sides)

if __name__ == '__main__':
    try:
        triangle = Triangle(7, 10, 5)
        print(triangle.perimeter())
        print(f"Sides: {triangle.sides}")
    except ValueError as e:
        print(e)