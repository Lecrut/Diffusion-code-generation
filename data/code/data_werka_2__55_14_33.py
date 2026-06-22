class Triangle:
    MIN_SIDE_LENGTH = 1

    @staticmethod
    def validate_side_length(side):
        if not isinstance(side, (int, float)):
            raise ValueError("Side length must be a number")
        if side <= Triangle.MIN_SIDE_LENGTH:
            raise ValueError("Side length must be greater than zero")

    def __init__(self, side1, side2, side3):
        Triangle.validate_side_length(side1)
        Triangle.validate_side_length(side2)
        Triangle.validate_side_length(side3)
        self.sides = [side1, side2, side3]

    def perimeter(self):
        return sum(self.sides)

if __name__ == '__main__':
    triangle_sides = (7, 10, 5)
    triangle = Triangle(*triangle_sides)
    print(triangle.perimeter())