import math

class Triangle:
    def __init__(self, dimensions):
        if 'base' not in dimensions or 'height' not in dimensions:
            raise ValueError("Dimensions must include both base and height.")
        self.base = dimensions['base']
        self.height = dimensions['height']

    def calculate_hypotenuse(self):
        return math.sqrt(self.base**2 + self.height**2)

    def calculate_area(self):
        return 0.5 * self.base * self.height

if __name__ == '__main__':
    triangle_properties = {
        'base': 6.0,
        'height': 8.0
    }
    triangle = Triangle(triangle_properties)
    hypotenuse = triangle.calculate_hypotenuse()
    area = triangle.calculate_area()
    print(f"Hypotenuse: {hypotenuse}")
    print(f"Area: {area}")