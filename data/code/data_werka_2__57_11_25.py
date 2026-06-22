class Triangle:
    def __init__(self, base, height):
        self.base = base
        self.height = height

    def calculate_area(self):
        return 0.5 * self.base * self.height

def main():
    triangle_config = {'base': 6, 'height': 8}
    triangle = Triangle(triangle_config['base'], triangle_config['height'])
    area = triangle.calculate_area()
    print(area)

if __name__ == '__main__':
    main()