import math
BASE = 6.0
HEIGHT = 8.0

class Triangle:

    def __init__(self, base, height):
        self.base = base
        self.height = height

    def calculate_hypotenuse(self):
        return math.sqrt(self.base ** 2 + self.height ** 2)

    def calculate_area(self):
        return 0.5 * self.base * self.height
if __name__ == '__main__':
    triangle = Triangle(BASE, HEIGHT)
    hypotenuse = triangle.calculate_hypotenuse()
    area = triangle.calculate_area()
    print(f'Hypotenuse: {hypotenuse}')
    print(f'Area: {area}')