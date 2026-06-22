class PairAverageCalculator:
    def __init__(self, pairs):
        self.pairs = pairs

    def calculate_averages(self):
        return tuple((a + b) / 2 for a, b in self.pairs)

if __name__ == '__main__':
    calculator = PairAverageCalculator([
        (1, 2),
        (3, 4),
        (5, 6)
    ])
    averages = calculator.calculate_averages()
    print(averages)