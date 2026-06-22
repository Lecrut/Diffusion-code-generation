class Triangle:
    def __init__(self, base, height):
        if base <= 0 or height <= 0:
            raise ValueError("Base and height must be positive numbers.")
        self.base = base
        self.height = height

    def area(self):
        return 0.5 * self.base * self.height

if __name__ == '__main__':
    triangle_dimensions = {'base': 9, 'height': 4}
    try:
        triangle = Triangle(triangle_dimensions['base'], triangle_dimensions['height'])
        print(f"Area of the triangle: {triangle.area()}")
    except ValueError as e:
        print(e)