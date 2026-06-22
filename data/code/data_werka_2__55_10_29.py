class Triangle:

    def __init__(self, side1, side2, side3):
        self.side1 = side1
        self.side2 = side2
        self.side3 = side3

    @property
    def perimeter(self):
        return self.calculate_perimeter()

    def calculate_perimeter(self):
        return self.side1 + self.side2 + self.side3
if __name__ == '__main__':
    side_a = 9
    side_b = 12
    side_c = 15
    triangle = Triangle(side_a, side_b, side_c)
    print(triangle.perimeter)