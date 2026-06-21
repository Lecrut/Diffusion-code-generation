class Shape:
    def __init__(self, side_lengths):
        if not isinstance(side_lengths, (list, tuple)):
            raise ValueError("Input must be a sequence of numbers")
        if len(side_lengths) < 3:
            raise ValueError("A shape must have at least 3 sides")
        validated_sides = []
        for length in side_lengths:
            if not isinstance(length, (int, float)):
                raise ValueError("All side lengths must be numeric")
            if length <= 0:
                raise ValueError("All side lengths must be positive")
            validated_sides.append(float(length))
        self.sides = tuple(validated_sides)

    def perimeter(self):
        total = 0.0
        for s in self.sides:
            total += s
        return total

    def area(self):
        n = len(self.sides)
        if n == 3:
            a, b, c = self.sides
            s = (a + b + c) / 2.0
            return (s * (s - a) * (s - b) * (s - c)) ** 0.5
        elif n == 4:
            a, b, c, d = self.sides
            s = (a + b + c + d) / 2.0
            return ((s - a) * (s - b) * (s - c) * (s - d)) ** 0.5
        else:
            raise ValueError("Area calculation only supported for triangles and quadrilaterals")

if __name__ == '__main__':
    triangle_sides = [3.0, 4.0, 5.0]
    triangle = Shape(triangle_sides)
    print(f"Triangle Perimeter: {triangle.perimeter()}")
    print(f"Triangle Area: {triangle.area()}")

    square_sides = [5.0, 5.0, 5.0, 5.0]
    square = Shape(square_sides)
    print(f"Square Perimeter: {square.perimeter()}")
    print(f"Square Area: {square.area()}")