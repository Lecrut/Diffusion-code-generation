class Triangle:
    def __init__(self, side1, side2, side3):
        if side1 + side2 <= side3 or side1 + side3 <= side2 or side2 + side3 <= side1:
            raise ValueError("Invalid triangle sides")
        self.side1 = side1
        self.side2 = side2
        self.side3 = side3

    def calculate_area(self):
        s = (self.side1 + self.side2 + self.side3) / 2
        area = (s * (s - self.side1) * (s - self.side2) * (s - self.side3)) ** 0.5
        return area

if __name__ == '__main__':
    try:
        triangle = Triangle(3, 4, 5)
        print(triangle.calculate_area())
    except ValueError as e:
        print(e)