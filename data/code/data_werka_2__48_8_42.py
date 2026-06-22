class Shape:
    _area_formulas = {
        3: lambda s: (s[0] + s[1] + s[2]) / 2,
        4: lambda s: s[0] * s[1],
        5: lambda s: (5 * s[0] ** 2) / (4 * (1 + (5 - 2 * 5) ** 0.5 / 2)),
    }

    def __init__(self, side_lengths):
        if not isinstance(side_lengths, (list, tuple)):
            raise ValueError("Side lengths must be a list or tuple")
        if len(side_lengths) < 3:
            raise ValueError("A shape must have at least 3 sides")
        validated = []
        for val in side_lengths:
            if not isinstance(val, (int, float)):
                raise ValueError("All side lengths must be numeric")
            if val <= 0:
                raise ValueError("All side lengths must be positive")
            validated.append(float(val))
        self.sides = tuple(validated)

    def perimeter(self):
        total = 0.0
        for side in self.sides:
            total += side
        return total

    def area(self):
        n = len(self.sides)
        if n in self._area_formulas:
            formula = self._area_formulas[n]
            return formula(self.sides)
        if n == 3:
            a, b, c = self.sides
            s = (a + b + c) / 2
            return (s * (s - a) * (s - b) * (s - c)) ** 0.5
        if n == 4:
            a, b, c, d = self.sides
            return a * b
        raise ValueError(f"Area calculation not supported for {n}-sided polygons in this implementation")

if __name__ == '__main__':
    triangle = Shape([3.0, 4.0, 5.0])
    print(triangle.perimeter())
    print(triangle.area())
    
    rectangle = Shape([5.0, 10.0])
    print(rectangle.perimeter())
    print(rectangle.area())