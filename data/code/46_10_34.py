class Triangle:

    def __init__(self, side1, side2, side3):
        self.side1 = side1
        self.side2 = side2
        self.side3 = side3
        if not self.is_valid_triangle():
            raise ValueError('The given sides do not form a valid triangle')

    def is_valid_triangle(self):
        return (self.side1 > 0 and self.side2 > 0 and (self.side3 > 0)) and self.side1 + self.side2 > self.side3 and (self.side1 + self.side3 > self.side2) and (self.side2 + self.side3 > self.side1)

    def perimeter(self):
        return self.side1 + self.side2 + self.side3
if __name__ == '__main__':
    try:
        triangle = Triangle(5.0, 6.0, 7.0)
        print(triangle.perimeter())
        print('Valid triangle:', triangle.is_valid_triangle())
    except ValueError as e:
        print(e)