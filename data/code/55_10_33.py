class Triangle:

    def __init__(self, side1, side2, side3):
        self.sides = [side1, side2, side3]

    @property
    def perimeter(self):
        return sum(self.sides)
if __name__ == '__main__':
    side_a = 5
    side_b = 7
    side_c = 9
    triangle = Triangle(side_a, side_b, side_c)
    calculated_perimeter = triangle.perimeter
    print(calculated_perimeter)