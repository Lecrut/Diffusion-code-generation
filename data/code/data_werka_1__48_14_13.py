import math

class RightAngledTriangle:
    def __init__(self, base, height):
        self.base = base
        self.height = height

    def calculate_hypotenuse(self):
        return math.sqrt(self.base ** 2 + self.height ** 2)

    def calculate_area(self):
        return (self.base * self.height) / 2

if __name__ == '__main__':
    triangle = RightAngledTriangle(6.0, 8.0)
    print("Hypotenuse:", triangle.calculate_hypotenuse())
    print("Area:", triangle.calculate_area())