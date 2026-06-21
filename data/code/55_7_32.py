class Triangle:
    MINIMUM_SIDE_LENGTH = 0.1

    @staticmethod
    def is_valid_triangle(a, b, c):
        return (a > Triangle.MINIMUM_SIDE_LENGTH and b > Triangle.MINIMUM_SIDE_LENGTH and c > Triangle.MINIMUM_SIDE_LENGTH) and \
               (a + b > c and a + c > b and b + c > a)

    def __init__(self, side1, side2, side3):
        if not Triangle.is_valid_triangle(side1, side2, side3):
            raise ValueError("The given sides do not form a valid triangle")
        self.side1 = side1
        self.side2 = side2
        self.side3 = side3

    def get_perimeter(self):
        return self.side1 + self.side2 + self.side3

if __name__ == '__main__':
    try:
        sample_sides = [9, 40, 41]
        triangle = Triangle(*sample_sides)
        print(triangle.get_perimeter())
    except ValueError as e:
        print(e)