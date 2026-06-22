class ParallelogramCalculator:
    def __init__(self, base, height):
        self.base = base
        self.height = height

    def get_area(self):
        if self.base <= 0 or self.height <= 0:
            raise ValueError("Inputs must be positive")
        if not isinstance(self.base, (int, float)) or not isinstance(self.height, (int, float)):
            raise TypeError("Inputs must be numeric")
        return self.base * self.height

    def get_dimensions(self):
        return self.base, self.height

if __name__ == '__main__':
    calc_one = ParallelogramCalculator(5, 10)
    calc_two = ParallelogramCalculator(7.5, 4.2)
    print(calc_one.get_area())
    print(calc_two.get_area())
    print(calc_one.get_dimensions())
    print(calc_two.get_dimensions())