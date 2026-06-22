class Shape:
    def __init__(self, sides):
        if not isinstance(sides, (list, tuple)):
            raise ValueError("Sides must be a list or tuple")
        if len(sides) < 3:
            raise ValueError("A shape must have at least 3 sides")
        validated = []
        for s in sides:
            if not isinstance(s, (int, float)):
                raise ValueError("Side lengths must be numeric")
            if s <= 0:
                raise ValueError("Side lengths must be positive")
            validated.append(s)
        self.sides = validated

    def get_perimeter(self):
        return sum(self.sides)

    def get_area(self):
        n = len(self.sides)
        if n == 3:
            a, b, c = self.sides
            s = (a + b + c) / 2.0
            val = s * (s - a) * (s - b) * (s - c)
            if val < 0:
                return 0.0
            return val ** 0.5
        if n == 4:
            a, b, c, d = self.sides
            s = (a + b + c + d) / 2.0
            val = (s - a) * (s - b) * (s - c) * (s - d)
            if val < 0:
                return 0.0
            return val ** 0.5
        return 0.0

if __name__ == '__main__':
    triangle = Shape([3, 4, 5])
    quad = Shape([5, 5, 5, 5])
    print(triangle.get_perimeter())
    print(triangle.get_area())
    print(quad.get_perimeter())
    print(quad.get_area())