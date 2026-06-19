class Triangle:
    def __init__(self, side1, side2, side3):
        if not self.is_valid_triangle(side1, side2, side3):
            raise ValueError("Invalid triangle side lengths")
        self.side1 = side1
        self.side2 = side2
        self.side3 = side3

    def is_valid_triangle(self, a, b, c):
        return a > 0 and b > 0 and c > 0 and a + b > c and a + c > b and b + c > a

    def get_perimeter(self):
        return self.side1 + self.side2 + self.side3

if __name__ == '__main__':
    try:
        triangle = Triangle(3, 4, 5)
        print(triangle.get_perimeter())
    except ValueError as e:
        print(e)

    try:
        invalid_triangle = Triangle(1, 2, 4)
        print(invalid_triangle.get_perimeter())
    except ValueError as e:
        print(e)