class Triangle:
    def __init__(self, side1, side2, side3):
        self.side1 = side1
        self.side2 = side2
        self.side3 = side3
        self._validate_sides()

    def _validate_sides(self):
        if not (self.side1 > 0 and self.side2 > 0 and self.side3 > 0):
            raise ValueError("All sides must be positive numbers.")
        if not (self.side1 + self.side2 > self.side3 and
                self.side1 + self.side3 > self.side2 and
                self.side2 + self.side3 > self.side1):
            raise ValueError("The given sides do not form a valid triangle.")

    def calculate_perimeter(self):
        return self._sum_sides()

    def _sum_sides(self):
        return self.side1 + self.side2 + self.side3

if __name__ == '__main__':
    side_a = 9
    side_b = 12
    side_c = 15
    triangle = Triangle(side_a, side_b, side_c)
    perimeter = triangle.calculate_perimeter()
    print(perimeter)