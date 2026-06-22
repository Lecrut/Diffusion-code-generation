class Triangle:

    def __init__(self, side1, side2, side3):
        self.side1 = side1
        self.side2 = side2
        self.side3 = side3
        self._validate_sides()

    def _validate_sides(self):
        if any((side <= 0 for side in [self.side1, self.side2, self.side3])):
            raise ValueError('Side lengths must be positive numbers.')
        if self.side1 + self.side2 <= self.side3 or self.side1 + self.side3 <= self.side2 or self.side2 + self.side3 <= self.side1:
            raise ValueError('The given side lengths do not form a valid triangle.')

    def calculate_perimeter(self):
        return self.side1 + self.side2 + self.side3
if __name__ == '__main__':
    try:
        t = Triangle(3, 4, 5)
        print(t.calculate_perimeter())
    except ValueError as e:
        print(e)