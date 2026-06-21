class Triangle:
    def __init__(self, side1, side2, side3):
        if not self._are_valid_sides(side1, side2, side3):
            raise ValueError("Invalid triangle sides")
        self.side1 = side1
        self.side2 = side2
        self.side3 = side3

    def _are_valid_sides(self, a, b, c):
        if not all(isinstance(x, (int, float)) and x > 0 for x in [a, b, c]):
            return False
        if a + b <= c or a + c <= b or b + c <= a:
            return False
        return True

    def get_perimeter(self):
        return self.side1 + self.side2 + self.side3

if __name__ == '__main__':
    try:
        triangle = Triangle(9, 40, 41)
        print(triangle.get_perimeter())
    except ValueError as e:
        print(e)