class Triangle:
    def __init__(self, dimensions):
        self.base = dimensions['base']
        self.height = dimensions['height']

    def calculate_area(self):
        return 0.5 * self.base * self.height

if __name__ == '__main__':
    triangle_dimensions = {'base': 6, 'height': 8}
    triangle = Triangle(triangle_dimensions)
    area = triangle.calculate_area()
    print(area)