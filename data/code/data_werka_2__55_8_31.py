class Triangle:

    def __init__(self, side1, side2, side3):
        self.sides = [side1, side2, side3]
        if not all((side > 0 for side in self.sides)):
            raise ValueError('All side lengths must be positive numbers.')

    def perimeter(self):
        return sum(self.sides)
if __name__ == '__main__':
    try:
        triangle = Triangle(5, 12, 13)
        print(triangle.perimeter())
        another_triangle = Triangle(7, 24, 25)
        print(another_triangle.perimeter())
    except ValueError as e:
        print(e)