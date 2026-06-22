class Triangle:
    def __init__(self, side1, side2, side3):
        self.side1 = side1
        self.side2 = side2
        self.side3 = side3

    @staticmethod
    def is_valid_triangle(side1, side2, side3):
        return (side1 + side2 > side3) and \
               (side1 + side3 > side2) and \
               (side2 + side3 > side1)

    def perimeter(self):
        if not Triangle.is_valid_triangle(self.side1, self.side2, self.side3):
            raise ValueError("Invalid triangle sides")
        return self.side1 + self.side2 + self.side3

if __name__ == '__main__':
    side1 = 7
    side2 = 10
    side3 = 5
    try:
        triangle = Triangle(side1, side2, side3)
        print(triangle.perimeter())
    except ValueError as e:
        print(e)