class Triangle:
    def __init__(self, side1, side2, side3):
        self.sides = [side1, side2, side3]
        self.validate_sides()

    def validate_sides(self):
        if not all(a + b > c for a, b, c in [
            (self.sides[0], self.sides[1], self.sides[2]),
            (self.sides[0], self.sides[2], self.sides[1]),
            (self.sides[1], self.sides[2], self.sides[0])
        ]):
            raise ValueError("Invalid triangle sides")

    def perimeter(self):
        return sum(self.sides)

if __name__ == '__main__':
    try:
        triangle = Triangle(3, 4, 5)
        print(triangle.perimeter())
    except ValueError as e:
        print(e)