class Triangle:
    def __init__(self, side1, side2, side3):
        self.sides = sorted([side1, side2, side3])
        if not all(isinstance(side, int) and side > 0 for side in self.sides):
            raise ValueError("All sides must be positive integers")
        if not (self.sides[0] + self.sides[1] > self.sides[2]):
            raise ValueError("Invalid triangle sides")

    def perimeter(self):
        return sum(self.sides)

if __name__ == '__main__':
    try:
        triangle = Triangle(7, 10, 5)
        print(triangle.perimeter())
    except ValueError as e:
        print(e)