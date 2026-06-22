class Triangle:
    MIN_SIDE_LENGTH = 0

    @staticmethod
    def is_valid_triangle(a, b, c):
        return all(isinstance(x, (int, float)) and x > Triangle.MIN_SIDE_LENGTH for x in [a, b, c]) and \
               a + b > c and a + c > b and b + c > a

    def __init__(self, side1, side2, side3):
        if not Triangle.is_valid_triangle(side1, side2, side3):
            raise ValueError("Invalid triangle sides")
        self.side1 = side1
        self.side2 = side2
        self.side3 = side3

    def get_perimeter(self):
        return self.side1 + self.side2 + self.side3

if __name__ == '__main__':
    try:
        triangle = Triangle(9, 12, 15)
        print(triangle.get_perimeter())
    except ValueError as e:
        print(e)