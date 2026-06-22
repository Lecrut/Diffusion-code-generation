class Triangle:
    def __init__(self, base, height):
        self.base = base
        self.height = height

    def area(self):
        return 0.5 * self.base * self.height

if __name__ == '__main__':
    dimensions = {'base': 6, 'height': 8}
    triangle = Triangle(dimensions['base'], dimensions['height'])
    print(triangle.area())