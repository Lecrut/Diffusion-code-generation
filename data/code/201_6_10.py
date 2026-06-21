class AverageCalculator:
    def __init__(self):
        self.total = 0
        self.count = 0

    def add(self, value):
        if not isinstance(value, (int, float)):
            raise ValueError("Input must be a number")
        self.total += value
        self.count += 1

    def compute_mean(self):
        if self.count == 0:
            return 0
        return self.total / self.count

if __name__ == '__main__':
    calculator = AverageCalculator()
    calculator.add(10)
    calculator.add(20)
    calculator.add(30)
    print(f"Computed Mean: {calculator.compute_mean()}")