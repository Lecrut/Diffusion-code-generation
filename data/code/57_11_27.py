class Triangle:
    def __init__(self, base, height):
        self.base = base
        self.height = height

    def calculate_area(self):
        return 0.5 * self.base * self.height

    def get_dimensions(self):
        return f"Base: {self.base}, Height: {self.height}"

if __name__ == '__main__':
    triangle = Triangle(6, 8)
    area = triangle.calculate_area()
    dimensions = triangle.get_dimensions()
    print(area)
    print(dimensions)