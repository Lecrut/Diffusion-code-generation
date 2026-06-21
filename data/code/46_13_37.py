class Triangle:

    def __init__(self, side1, side2, side3):
        self.side1 = side1
        self.side2 = side2
        self.side3 = side3
        self.validate_sides()

    def validate_sides(self):
        MIN_SIDE_LENGTH = 0.0001
        if not (self.side1 > MIN_SIDE_LENGTH and self.side2 > MIN_SIDE_LENGTH and (self.side3 > MIN_SIDE_LENGTH)):
            raise ValueError('All sides must be greater than the minimum threshold.')
        if not (self.side1 + self.side2 > self.side3 and self.side1 + self.side3 > self.side2 and (self.side2 + self.side3 > self.side1)):
            raise ValueError('The given sides do not form a valid triangle.')

    def calculate_perimeter(self):
        return self.side1 + self.side2 + self.side3
if __name__ == '__main__':
    try:
        triangle = Triangle(9, 12, 15)
        perimeter = triangle.calculate_perimeter()
        print(perimeter)
    except ValueError as e:
        print(e)