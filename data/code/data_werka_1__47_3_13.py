class Triangle:
    def __init__(self, side1, side2, side3):
        self.side1 = side1
        self.side2 = side2
        self.side3 = side3
        if not self.is_valid_triangle():
            raise ValueError("Invalid triangle sides")

    def is_valid_triangle(self):
        return (self.side1 + self.side2 > self.side3 and
                self.side1 + self.side3 > self.side2 and
                self.side2 + self.side3 > self.side1)

    @staticmethod
    def calculate_area(side1, side2, side3):
        if not Triangle.is_valid_triangle_static(side1, side2, side3):
            raise ValueError("Invalid triangle sides")
        s = (side1 + side2 + side3) / 2
        area = (s * (s - side1) * (s - side2) * (s - side3)) ** 0.5
        return area

    @staticmethod
    def is_valid_triangle_static(side1, side2, side3):
        return (side1 + side2 > side3 and
                side1 + side3 > side2 and
                side2 + side3 > side1)

if __name__ == '__main__':
    try:
        triangle = Triangle(6, 8, 10)
        print(triangle.calculate_area(triangle.side1, triangle.side2, triangle.side3))
    except ValueError as e:
        print(e)