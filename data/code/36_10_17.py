class Trapezoid:
    def __init__(self, base1, base2, height):
        if base1 <= 0 or base2 <= 0 or height <= 0:
            raise ValueError("Dimensions must be positive numbers")
        self.base1 = float(base1)
        self.base2 = float(base2)
        self.height = float(height)

    def area(self):
        return 0.5 * (self.base1 + self.base2) * self.height

    def perimeter(self, side1, side2):
        if side1 <= 0 or side2 <= 0:
            raise ValueError("Side lengths must be positive numbers")
        return self.base1 + self.base2 + side1 + side2

if __name__ == '__main__':
    t = Trapezoid(5, 7, 4)
    print(t.area())
    print(t.perimeter(3, 3))