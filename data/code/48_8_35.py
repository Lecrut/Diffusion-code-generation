class Shape:
    def __init__(self, sides):
        if not isinstance(sides, list):
            raise ValueError("Sides must be a list")
        if len(sides) < 3:
            raise ValueError("A shape must have at least 3 sides")
        for side in sides:
            if side <= 0:
                raise ValueError("Side lengths must be positive")
        self.sides = sides

    def perimeter(self):
        return sum(self.sides)

    def area(self):
        n = len(self.sides)
        if n == 3:
            a, b, c = self.sides
            s = (a + b + c) / 2
            return (s * (s - a) * (s - b) * (s - c)) ** 0.5
        elif n == 4:
            a, b, c, d = self.sides
            s = (a + b + c + d) / 2
            return ((s - a) * (s - b) * (s - c) * (s - d)) ** 0.5
        else:
            raise ValueError("Area calculation is only supported for triangles and quadrilaterals")

if __name__ == '__main__':
    triangle = Shape([3, 4, 5])
    print(f"Triangle Perimeter: {triangle.perimeter()}")
    print(f"Triangle Area: {triangle.area()}")

    square = Shape([5, 5, 5, 5])
    print(f"Square Perimeter: {square.perimeter()}")
    print(f"Square Area: {square.area()}")