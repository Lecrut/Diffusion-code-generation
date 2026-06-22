import math

class RightAngledTriangle:
    def __init__(self, leg1, leg2, hypotenuse):
        self.leg1 = leg1
        self.leg2 = leg2
        self.hypotenuse = hypotenuse

    def is_right_angled(self):
        return math.isclose(self.leg1**2 + self.leg2**2, self.hypotenuse**2)

    def get_sides(self):
        return (self.leg1, self.leg2, self.hypotenuse)

if __name__ == '__main__':
    sample_leg1 = 3
    sample_leg2 = 4
    sample_hypotenuse = 5

    triangle = RightAngledTriangle(sample_leg1, sample_leg2, sample_hypotenuse)
    print(triangle.is_right_angled())
    print(triangle.get_sides())