class Trapezoid:
    def __init__(self, base1, base2, leg1, leg2):
        self.base1 = base1
        self.base2 = base2
        self.leg1 = leg1
        self.leg2 = leg2

    def perimeter(self):
        return self.base1 + self.base2 + self.leg1 + self.leg2

if __name__ == '__main__':
    trapezoid = Trapezoid(5, 7, 3, 4)
    print(trapezoid.perimeter())