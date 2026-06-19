class Triangle:
    def __init__(self, side1, side2, side3):
        if not self._are_sides_valid(side1, side2, side3):
            raise ValueError("Invalid triangle sides")
        self.side1 = side1
        self.side2 = side2
        self.side3 = side3

    def _are_sides_valid(self, a, b, c):
        return a > 0 and b > 0 and c > 0 and (a + b > c) and (a + c > b) and (b + c > a)

    def perimeter(self):
        return self.side1 + self.side2 + self.side3

if __name__ == '__main__':
    try:
        triangle = Triangle(6, 8, 10)
        print(triangle.perimeter())
    except ValueError as e:
        print(e)