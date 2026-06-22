class Trapezoid:
    def __init__(self, base_a, base_b, height):
        if base_a <= 0 or base_b <= 0 or height <= 0:
            raise ValueError("Base and height values must be positive.")
        self.base_a = base_a
        self.base_b = base_b
        self.height = height

    def area(self):
        return (self.base_a + self.base_b) * self.height / 2

if __name__ == '__main__':
    t = Trapezoid(5, 7, 3)
    print(t.area())