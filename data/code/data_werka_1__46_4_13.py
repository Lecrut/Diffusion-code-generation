class Triangle:

    def __init__(self, side1, side2, side3):
        self.sides = [side1, side2, side3]
        if not all((isinstance(side, int) and side > 0 for side in self.sides)):
            raise ValueError('Side lengths must be positive integers')
        if not (self.sides[0] + self.sides[1] > self.sides[2] and self.sides[0] + self.sides[2] > self.sides[1] and (self.sides[1] + self.sides[2] > self.sides[0])):
            raise ValueError('Invalid triangle sides')

    def perimeter(self):
        return sum(self.sides)
if __name__ == '__main__':
    try:
        triangle = Triangle(7, 9, 12)
        print(triangle.perimeter())
        print(triangle.sides)
    except ValueError as e:
        print(e)