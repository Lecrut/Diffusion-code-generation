class Trapezoid:
    def __init__(self, base_a, base_b, height):
        if not isinstance(base_a, (int, float)) or not isinstance(base_b, (int, float)) or not isinstance(height, (int, float)):
            raise TypeError("All dimensions must be numbers")
        if base_a <= 0 or base_b <= 0 or height <= 0:
            raise ValueError("All dimensions must be positive")
        self.base_a = float(base_a)
        self.base_b = float(base_b)
        self.height = float(height)

    def area(self):
        return 0.5 * (self.base_a + self.base_b) * self.height

if __name__ == '__main__':
    t1 = Trapezoid(10, 15, 4)
    print(t1.area())
    t2 = Trapezoid(5.5, 8.5, 3.0)
    print(t2.area())