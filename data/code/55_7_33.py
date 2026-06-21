class Triangle:
    MIN_SIDE_LENGTH = 0

    def __init__(self, side1, side2, side3):
        self._validate_sides(side1, side2, side3)
        self.side1 = side1
        self.side2 = side2
        self.side3 = side3

    def _validate_sides(self, a, b, c):
        if not all(isinstance(x, (int, float)) and x > Triangle.MIN_SIDE_LENGTH for x in [a, b, c]):
            raise ValueError("Side lengths must be positive numbers")
        if a + b <= c or a + c <= b or b + c <= a:
            raise ValueError("The given sides do not form a valid triangle")

    def get_perimeter(self):
        return self.side1 + self.side2 + self.side3

if __name__ == '__main__':
    try:
        side_a = 9
        side_b = 40
        side_c = 41
        triangle = Triangle(side_a, side_b, side_c)
        print(triangle.get_perimeter())
    except ValueError as e:
        print(e)