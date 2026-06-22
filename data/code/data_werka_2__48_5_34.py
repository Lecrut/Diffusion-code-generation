import math

class Triangle:
    def __init__(self, leg1, leg2, hypotenuse):
        self.leg1 = leg1
        self.leg2 = leg2
        self.hypotenuse = hypotenuse
        self.validate()

    def validate(self):
        if self.hypotenuse <= self.leg1 or self.hypotenuse <= self.leg2:
            raise ValueError('Hypotenuse must be the longest side.')
        if not math.isclose(self.leg1**2 + self.leg2**2, self.hypotenuse**2):
            raise ValueError('The given sides do not form a right-angled triangle.')

    def get_sides(self):
        return (self.leg1, self.leg2, self.hypotenuse)

if __name__ == '__main__':
    try:
        triangle = Triangle(6, 8, 10)
        print(triangle.get_sides())
    except ValueError as e:
        print(e)