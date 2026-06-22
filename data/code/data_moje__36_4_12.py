class Trapezoid:
    def __init__(self, base1, base2, height):
        self.base1 = base1
        self.base2 = base2
        self.height = height

    def area(self):
        return (self.base1 + self.base2) * self.height / 2

if __name__ == '__main__':
    t = Trapezoid(5, 10, 6)
    print(t.area())