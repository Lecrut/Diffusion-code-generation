class SumCalculator:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def compute_sum(self):
        return self.x + self.y

if __name__ == '__main__':
    calc = SumCalculator(12, 18)
    result = calc.compute_sum()
    print(result)