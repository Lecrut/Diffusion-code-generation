class MeanCalculator:
    def __init__(self):
        self.total = 0
        self.count = 0

    def add(self, value):
        self.total += value
        self.count += 1

    def calculate_mean(self):
        if self.count == 0:
            return 0
        return self.total / self.count

if __name__ == '__main__':
    calculator = MeanCalculator()
    sample_values = [10, 20, 30, 40, 50]
    for value in sample_values:
        calculator.add(value)
    print(calculator.calculate_mean())