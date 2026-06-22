class Triangle:
    def __init__(self, base, height):
        self.base = base
        self.height = height

    def calculate_area(self):
        return 0.5 * self.base * self.height

if __name__ == '__main__':
    triangle_properties = {'base': 6, 'height': 8}
    triangle = Triangle(triangle_properties['base'], triangle_properties['height'])
    area = triangle.calculate_area()
    print(area)