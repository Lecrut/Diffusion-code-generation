import math

class Shape:
    MIN_SIDES = 3
    VALID_TYPES = (int, float)

    def __init__(self, side_lengths):
        if not isinstance(side_lengths, (list, tuple)):
            raise ValueError("Side lengths must be a list or tuple")
        if len(side_lengths) < self.MIN_SIDES:
            raise ValueError("A shape must have at least 3 sides")
        self.sides = []
        for length in side_lengths:
            if not isinstance(length, self.VALID_TYPES):
                raise ValueError("Side lengths must be numeric")
            if length <= 0:
                raise ValueError("Side lengths must be positive")
            self.sides.append(float(length))

    def perimeter(self):
        return sum(self.sides)

    def area(self):
        n = len(self.sides)
        if n == 3:
            a, b, c = self.sides
            s = self.perimeter() / 2
            return math.sqrt(s * (s - a) * (s - b) * (s - c))
        if n == 4:
            a, b, c, d = self.sides
            s = self.perimeter() / 2
            return math.sqrt((s - a) * (s - b) * (s - c) * (s - d))
        raise ValueError("Area calculation only supported for triangles and quadrilaterals")

if __name__ == '__main__':
    triangle = Shape([3, 4, 5])
    print(f"Triangle Perimeter: {triangle.perimeter()}")
    print(f"Triangle Area: {triangle.area()}")
    square = Shape([5, 5, 5, 5])
    print(f"Square Perimeter: {square.perimeter()}")
    print(f"Square Area: {square.area()}")