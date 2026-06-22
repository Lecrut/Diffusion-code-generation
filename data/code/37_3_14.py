class ParallelogramCalculator:
    def __init__(self, base, height):
        self.base = base
        self.height = height

    def get_area(self):
        return float(self.base * self.height)

if __name__ == '__main__':
    calc = ParallelogramCalculator(12.5, 8.0)
    print(calc.get_area())
    calc.base = 10.0
    print(calc.get_area())