class Triangle:
    MIN_SIDE_LENGTH = 1

    def __init__(self, side1, side2, side3):
        if not all(side >= Triangle.MIN_SIDE_LENGTH for side in (side1, side2, side3)):
            raise ValueError("Side lengths must be at least {}".format(Triangle.MIN_SIDE_LENGTH))
        if not (side1 + side2 > side3 and side1 + side3 > side2 and side2 + side3 > side1):
            raise ValueError("The given sides do not form a valid triangle")
        self.sides = [side1, side2, side3]

    @property
    def perimeter(self):
        return sum(self.sides)

if __name__ == '__main__':
    try:
        triangle = Triangle(5, 6, 7)
        print(triangle.perimeter)
    except ValueError as e:
        print(e)