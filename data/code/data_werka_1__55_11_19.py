class Triangle:
    def __init__(self, side1, side2, side3):
        if all(side > 0 for side in [side1, side2, side3]):
            self.side1 = side1
            self.side2 = side2
            self.side3 = side3
        else:
            raise ValueError("All sides must be positive numbers")

    @property
    def perimeter(self):
        return self.side1 + self.side2 + self.side3

if __name__ == '__main__':
    try:
        triangle = Triangle(3, 4, 5)
        print(triangle.perimeter)
    except ValueError as e:
        print(e)

    try:
        invalid_triangle = Triangle(-1, 4, 5)
        print(invalid_triangle.perimeter)
    except ValueError as e:
        print(e)