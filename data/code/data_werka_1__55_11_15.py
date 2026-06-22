class Triangle:
    def __init__(self, side1, side2, side3):
        if side1 <= 0 or side2 <= 0 or side3 <= 0:
            raise ValueError("All sides must be positive numbers")
        self.side1 = side1
        self.side2 = side2
        self.side3 = side3

    @property
    def perimeter(self):
        return self.side1 + self.side2 + self.side3

if __name__ == '__main__':
    try:
        triangle_valid = Triangle(3, 4, 5)
        print(triangle_valid.perimeter)
    except ValueError as e:
        print(e)

    try:
        triangle_invalid = Triangle(-1, 4, 5)
    except ValueError as e:
        print(e)