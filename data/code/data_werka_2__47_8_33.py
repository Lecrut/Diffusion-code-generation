class Triangle:
    def __init__(self, base, height):
        if base <= 0 or height <= 0:
            raise ValueError("Base and height must be positive numbers.")
        self.base = base
        self.height = height

    def area(self):
        return 0.5 * self.base * self.height

if __name__ == '__main__':
    triangle_configurations = [
        {'base': 9, 'height': 4},
        {'base': 15, 'height': 6}
    ]

    for config in triangle_configurations:
        try:
            triangle = Triangle(config['base'], config['height'])
            print(f"Area of triangle with base {config['base']} and height {config['height']}: {triangle.area()}")
        except ValueError as e:
            print(e)