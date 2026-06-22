class ParallelogramCalculator:
    def __init__(self, base, height):
        self.base = base
        self.height = height

    def calculate_area(self):
        return self.base * self.height

def calculate_parallelogram_area(base, height):
    return base * height

if __name__ == '__main__':
    calc = ParallelogramCalculator(5.0, 3.0)
    print(calc.calculate_area())
    print(calculate_parallelogram_area(5.0, 3.0))