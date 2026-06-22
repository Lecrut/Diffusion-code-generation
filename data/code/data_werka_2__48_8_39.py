class Shape:
    def __init__(self, side_lengths):
        if not isinstance(side_lengths, (list, tuple)):
            raise ValueError("Side lengths must be a list or tuple")
        if len(side_lengths) < 3:
            raise ValueError("A shape must have at least 3 sides")
        numeric_sides = []
        for length in side_lengths:
            if not isinstance(length, (int, float)):
                raise ValueError("Side lengths must be numeric")
            if length <= 0:
                raise ValueError("Side lengths must be positive")
            numeric_sides.append(float(length))
        self.sides = tuple(numeric_sides)

    def calculate_perimeter(self):
        total = 0.0
        for s in self.sides:
            total += s
        return total

    def calculate_area(self):
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
            raise ValueError("Area calculation only supported for triangles and quadrilaterals")

if __name__ == '__main__':
    triangle = Shape([3, 4, 5])
    print(triangle.calculate_perimeter())
    print(triangle.calculate_area())
    rectangle = Shape([5, 10, 5, 10])
    print(rectangle.calculate_perimeter())
    print(rectangle.calculate_area())