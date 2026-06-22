class Triangle:
    def __init__(self, side1, side2, side3):
        self.side1 = side1
        self.side2 = side2
        self.side3 = side3
        self.validate_sides()

    @staticmethod
    def is_valid_triangle(side1, side2, side3):
        return (side1 > 0 and side2 > 0 and side3 > 0) and \
               (side1 + side2 > side3 and
                side1 + side3 > side2 and
                side2 + side3 > side1)

    def validate_sides(self):
        if not Triangle.is_valid_triangle(self.side1, self.side2, self.side3):
            raise ValueError("The given sides do not form a valid triangle.")

    def calculate_perimeter(self):
        return self.side1 + self.side2 + self.side3

if __name__ == '__main__':
    try:
        triangle = Triangle(9, 12, 15)
        perimeter = triangle.calculate_perimeter()
        print(perimeter)
    except ValueError as e:
        print(e)