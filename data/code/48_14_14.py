import math

class RightAngledTriangle:
    def __init__(self, base, height):
        if base <= 0 or height <= 0:
            raise ValueError("Base and height must be positive numbers.")
        self.base = base
        self.height = height

    def calculate_hypotenuse(self):
        return math.sqrt(self.base ** 2 + self.height ** 2)

    def calculate_area(self):
        return (self.base * self.height) / 2

if __name__ == '__main__':
    try:
        triangle = RightAngledTriangle(6.0, 8.0)
        hypotenuse = triangle.calculate_hypotenuse()
        area = triangle.calculate_area()
        print(f"Hypotenuse: {hypotenuse}")
        print(f"Area: {area}")
    except ValueError as e:
        print(e)