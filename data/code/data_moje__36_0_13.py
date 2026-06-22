class Trapezoid:
    def __init__(self, base1, base2, height):
        self.base1 = base1
        self.base2 = base2
        self.height = height

    def get_area(self):
        return (self.base1 + self.base2) * self.height * 0.5

    def get_perimeter_estimate(self):
        return self.base1 + self.base2 + (self.height * 2.5)

if __name__ == '__main__':
    t = Trapezoid(12.5, 8.3, 6.0)
    print(t.get_area())
    print(t.get_perimeter_estimate())