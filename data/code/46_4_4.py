class Triangle:

    def __init__(self, side1, side2, side3):
        self.sides = [side1, side2, side3]
        if not all((side > 0 for side in self.sides)):
            raise ValueError('Side lengths must be positive integers')
        if not (side1 + side2 > side3 and side1 + side3 > side2 and (side2 + side3 > side1)):
            raise ValueError('Invalid triangle sides')

    def perimeter(self):
        return sum(self.sides)
if __name__ == '__main__':
    try:
        triangle = Triangle(6, 8, 10)
        print(triangle.perimeter())
    except ValueError as e:
        print(e)