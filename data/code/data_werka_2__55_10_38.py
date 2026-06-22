class Triangle:
    def __init__(self, side1, side2, side3):
        self.side1 = side1
        self.side2 = side2
        self.side3 = side3

    @property
    def perimeter(self):
        return sum([self.side1, self.side2, self.side3])

if __name__ == '__main__':
    triangle = Triangle(5, 6, 7)
    print(triangle.perimeter)