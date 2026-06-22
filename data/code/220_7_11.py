class AverageCalculator:
    def __init__(self):
        self.total = 0
        self.count = 0

    def add(self, value):
        self.total += value
        self.count += 1

    def get_average(self):
        if self.count == 0:
            return 0
        return self.total / self.count

if __name__ == '__main__':
    calculator = AverageCalculator()
    for value in [10, 20, 30, 40, 50]:
        calculator.add(value)
    print(calculator.get_average())