class Triangle:

    def __init__(self, side1, side2, side3):
        self.side1 = side1
        self.side2 = side2
        self.side3 = side3
        if not self.is_valid_triangle():
            raise ValueError('Invalid triangle side lengths')

    def is_valid_triangle(self):
        return self.side1 + self.side2 > self.side3 and self.side1 + self.side3 > self.side2 and (self.side2 + self.side3 > self.side1) and (self.side1 > 0) and (self.side2 > 0) and (self.side3 > 0)

    def get_perimeter(self):
        return self.side1 + self.side2 + self.side3
if __name__ == '__main__':
    triangle1 = Triangle(3, 4, 5)
    print(triangle1.get_perimeter())
    triangle2 = Triangle(7, 8, 9)
    print(triangle2.get_perimeter())
    try:
        invalid_triangle = Triangle(1, 2, 3)
    except ValueError as e:
        print(e)