class Trapezoid:
    def __init__(self, base_a, base_b, height):
        if base_a <= 0 or base_b <= 0 or height <= 0:
            raise ValueError("All dimensions must be positive numbers.")
        self.base_a = float(base_a)
        self.base_b = float(base_b)
        self.height = float(height)

    def area(self):
        return 0.5 * (self.base_a + self.base_b) * self.height

if __name__ == '__main__':
    t = Trapezoid(10, 20, 5)
    print(t.area())