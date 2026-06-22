class Trapezoid:
    def __init__(self, base1, base2, height):
        if not all(isinstance(x, (int, float)) for x in (base1, base2, height)):
            raise TypeError("All dimensions must be numbers.")
        if base1 <= 0 or base2 <= 0 or height <= 0:
            raise ValueError("Dimensions must be positive.")
        self.base1 = base1
        self.base2 = base2
        self.height = height

    def area(self):
        return 0.5 * (self.base1 + self.base2) * self.height

if __name__ == '__main__':
    t = Trapezoid(10, 20, 5)
    print(t.area())