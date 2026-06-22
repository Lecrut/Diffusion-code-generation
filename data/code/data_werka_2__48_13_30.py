import math

class Triangle:

    def __init__(self, base, height):
        if base <= 0 or height <= 0:
            raise ValueError('Base and height must be positive numbers.')
        self.base = base
        self.height = height

    def calculate_hypotenuse(self):
        return math.sqrt(self.base ** 2 + self.height ** 2)

    def calculate_area(self):
        return 0.5 * self.base * self.height
if __name__ == '__main__':
    base_length = 10.0
    height_length = 4.0
    triangle = Triangle(base_length, height_length)
    hypotenuse_length = triangle.calculate_hypotenuse()
    area_size = triangle.calculate_area()
    print(f'Hypotenuse: {hypotenuse_length}')
    print(f'Area: {area_size}')