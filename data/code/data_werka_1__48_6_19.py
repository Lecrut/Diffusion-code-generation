import math

class RightTriangle:
    def __init__(self, leg1, leg2, hypotenuse):
        self.leg1 = leg1
        self.leg2 = leg2
        self.hypotenuse = hypotenuse
        self.validate_triangle()

    def validate_triangle(self):
        if not (self.hypotenuse > self.leg1 and self.hypotenuse > self.leg2):
            raise ValueError("Hypotenuse must be the longest side.")
        if not math.isclose(self.hypotenuse**2, self.leg1**2 + self.leg2**2, rel_tol=1e-9):
            raise ValueError("The sides do not form a right-angled triangle.")

    def get_side_lengths(self):
        return self.leg1, self.leg2, self.hypotenuse

if __name__ == '__main__':
    sample_leg1 = 3
    sample_leg2 = 4
    sample_hypotenuse = 5
    try:
        triangle = RightTriangle(sample_leg1, sample_leg2, sample_hypotenuse)
        side_lengths = triangle.get_side_lengths()
        print(side_lengths)
    except ValueError as e:
        print(e)