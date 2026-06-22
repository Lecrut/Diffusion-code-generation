class TriangleMetrics:
    def __init__(self, base, height):
        self.base = base
        self.height = height

    def compute_area(self):
        return 0.5 * self.base * self.height

    def describe_dimensions(self):
        return f"Triangle with base {self.base} and height {self.height}"

if __name__ == '__main__':
    triangle = TriangleMetrics(6, 8)
    print(triangle.describe_dimensions())
    print("Area:", triangle.compute_area())