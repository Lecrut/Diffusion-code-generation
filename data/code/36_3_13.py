class Trapezoid:
    def __init__(self, base1, base2, height):
        self.base1 = base1
        self.base2 = base2
        self.height = height

    def get_area(self):
        return (self.base1 + self.base2) * self.height / 2

if __name__ == '__main__':
    sample1 = Trapezoid(12, 18, 5)
    print(sample1.get_area())
    sample2 = Trapezoid(2.5, 4.5, 3.0)
    print(sample2.get_area())