class Triangle:
    def __init__(self, side1, side2, side3):
        if side1 > 0 and side2 > 0 and side3 > 0:
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
        triangle1 = Triangle(3, 4, 5)
        print(triangle1.perimeter)
    except ValueError as e:
        print(e)

    try:
        triangle2 = Triangle(-1, 4, 5)
        print(triangle2.perimeter)
    except ValueError as e:
        print(e)