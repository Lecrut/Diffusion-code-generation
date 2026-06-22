class TriangleGeometry:
    def __init__(self, base, height):
        self.base = base
        self.height = height

    def compute_area(self):
        return 0.5 * self.base * self.height

    def display_dimensions(self):
        return f"Base: {self.base}, Height: {self.height}"

if __name__ == '__main__':
    triangle = TriangleGeometry(6, 8)
    print(triangle.display_dimensions())
    print("Area:", triangle.compute_area())