class SumCalculator:
    def __init__(self, start, end):
        self.start = start
        self.end = end

    def calculate_sum(self):
        return sum(x for x in range(self.start, self.end + 1))

if __name__ == '__main__':
    calculator = SumCalculator(1, 100)
    total_sum = calculator.calculate_sum()
    print(total_sum)