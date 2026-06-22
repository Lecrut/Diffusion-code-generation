class Trapezoid:
    def __init__(self, base1, base2, height):
        if base1 <= 0 or base2 <= 0 or height <= 0:
            raise ValueError("Base and height must be positive numbers.")
        self.base1 = float(base1)
        self.base2 = float(base2)
        self.height = float(height)

    def area(self):
        return 0.5 * (self.base1 + self.base2) * self.height

if __name__ == '__main__':
    t = Trapezoid(10.0, 20.0, 5.0)
    print(t.area())