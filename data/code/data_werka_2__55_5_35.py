class Triangle:
    def __init__(self, side1, side2, side3):
        self.side1 = side1
        self.side2 = side2
        self.side3 = side3
        self.validate_sides()

    @staticmethod
    def validate_triangle(a, b, c):
        return a + b > c and a + c > b and b + c > a

    def validate_sides(self):
        if not Triangle.validate_triangle(self.side1, self.side2, self.side3):
            raise ValueError("Invalid triangle sides")

    def perimeter(self):
        return self.side1 + self.side2 + self.side3

if __name__ == '__main__':
    try:
        triangle = Triangle(6, 8, 10)
        print(triangle.perimeter())
    except ValueError as e:
        print(e)