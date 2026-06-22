import math

class RightAngledTriangle:
    def __init__(self, leg1, leg2, hypotenuse):
        self.leg1 = leg1
        self.leg2 = leg2
        self.hypotenuse = hypotenuse
        if not self.is_valid():
            raise ValueError("Invalid triangle sides")

    def is_valid(self):
        return math.isclose(self.hypotenuse ** 2, self.leg1 ** 2 + self.leg2 ** 2)

    def get_legs(self):
        return (self.leg1, self.leg2)

    def get_hypotenuse(self):
        return self.hypotenuse

if __name__ == '__main__':
    triangle = RightAngledTriangle(3, 4, 5)
    print(triangle.get_legs())
    print(triangle.get_hypotenuse())