class Triangle:
    def __init__(self, side1, side2, side3):
        self.side1 = side1
        self.side2 = side2
        self.side3 = side3
        self._validate_sides()

    def _validate_sides(self):
        if not all(side > 0 for side in (self.side1, self.side2, self.side3)):
            raise ValueError("Side lengths must be positive numbers.")

    @staticmethod
    def calculate_perimeter(side1, side2, side3):
        return side1 + side2 + side3

if __name__ == '__main__':
    try:
        triangle = Triangle(3, 4, 5)
        perimeter = Triangle.calculate_perimeter(triangle.side1, triangle.side2, triangle.side3)
        print(perimeter)
    except ValueError as e:
        print(e)