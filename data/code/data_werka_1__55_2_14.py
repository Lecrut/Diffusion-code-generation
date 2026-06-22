class Triangle:

    def __init__(self, side1, side2, side3):
        self.side1 = side1
        self.side2 = side2
        self.side3 = side3
        self._validate_sides()

    def _validate_sides(self):
        if not (self.side1 + self.side2 > self.side3 and self.side1 + self.side3 > self.side2 and (self.side2 + self.side3 > self.side1)):
            raise ValueError('The given side lengths do not form a valid triangle.')

    def perimeter(self):
        return self.side1 + self.side2 + self.side3
if __name__ == '__main__':
    try:
        t1 = Triangle(3, 4, 5)
        print(f'Perimeter of triangle (3, 4, 5): {t1.perimeter()}')
        t2 = Triangle(7, 10, 5)
        print(f'Perimeter of triangle (7, 10, 5): {t2.perimeter()}')
        t3 = Triangle(1, 2, 10)
    except ValueError as e:
        print(e)