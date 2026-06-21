class Triangle:
    def __init__(self, side1, side2, side3):
        if not all(isinstance(x, (int, float)) and x > 0 for x in [side1, side2, side3]):
            raise ValueError("Side lengths must be positive numbers")
        if side1 + side2 <= side3 or side1 + side3 <= side2 or side2 + side3 <= side1:
            raise ValueError("The given sides do not form a valid triangle")
        self.sides = [side1, side2, side3]

    def get_perimeter(self):
        return sum(self.sides)

if __name__ == '__main__':
    try:
        triangle = Triangle(9, 40, 41)
        print(triangle.get_perimeter())
    except ValueError as e:
        print(e)