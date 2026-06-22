class Triangle:
    def __init__(self, side1, side2, side3):
        self.side1 = side1
        self.side2 = side2
        self.side3 = side3

    def calculate_perimeter(self):
        return self.side1 + self.side2 + self.side3

if __name__ == '__main__':
    triangle = Triangle(7, 10, 5)
    print(triangle.calculate_perimeter())