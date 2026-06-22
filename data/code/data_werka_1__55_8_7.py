class Triangle:

    def __init__(self, side1, side2, side3):
        if not self.is_valid_triangle(side1, side2, side3):
            raise ValueError('Invalid triangle side lengths')
        self.side1 = side1
        self.side2 = side2
        self.side3 = side3

    def is_valid_triangle(self, a, b, c):
        return a + b > c and a + c > b and (b + c > a) and (a > 0) and (b > 0) and (c > 0)

    def get_perimeter(self):
        return self.side1 + self.side2 + self.side3
if __name__ == '__main__':
    triangle1 = Triangle(3, 4, 5)
    print(triangle1.get_perimeter())
    triangle2 = Triangle(5, 5, 5)
    print(triangle2.get_perimeter())
    try:
        invalid_triangle = Triangle(1, 2, 4)
    except ValueError as e:
        print(e)