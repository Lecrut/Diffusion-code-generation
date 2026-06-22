class Shape:
    def __init__(self, side_lengths):
        if not hasattr(side_lengths, '__iter__'):
            raise ValueError("Side lengths must be iterable")
        self.sides = []
        for length in side_lengths:
            if not isinstance(length, (int, float)):
                raise ValueError("Side lengths must be numeric")
            if length <= 0:
                raise ValueError("Side lengths must be positive")
            self.sides.append(float(length))
        if len(self.sides) < 3:
            raise ValueError("A shape must have at least 3 sides")

    def get_perimeter(self):
        return sum(self.sides)

    def get_area(self):
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
            return 0.0

if __name__ == '__main__':
    triangle = Shape([3, 4, 5])
    print(triangle.get_perimeter())
    print(triangle.get_area())
    square = Shape([5, 5, 5, 5])
    print(square.get_perimeter())
    print(square.get_area())