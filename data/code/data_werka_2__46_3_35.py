class Triangle:
    def __init__(self, side1, side2, side3):
        if not all(isinstance(side, int) and side > 0 for side in (side1, side2, side3)):
            raise ValueError("All sides must be positive integers.")
        self.sides = [side1, side2, side3]

    def perimeter(self):
        return sum(self.sides)

if __name__ == '__main__':
    try:
        triangle = Triangle(7, 24, 25)
        print(triangle.perimeter())
    except ValueError as e:
        print(e)