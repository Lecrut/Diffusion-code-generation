class Triangle:

    def __init__(self, side1, side2, side3):
        self.sides = [side1, side2, side3]

    @property
    def perimeter(self):
        return sum(self.sides)
if __name__ == '__main__':
    side_a = 9
    side_b = 12
    side_c = 15
    triangle = Triangle(side_a, side_b, side_c)
    result = triangle.perimeter
    print(result)