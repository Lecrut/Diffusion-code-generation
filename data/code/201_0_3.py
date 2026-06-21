class AverageCalculator:
    def __init__(self, numbers):
        self.numbers = numbers

    def calculate_average(self):
        if not self.numbers:
            return None
        total = sum(self.numbers)
        count = len(self.numbers)
        mean = total / count
        return mean

if __name__ == '__main__':
    sample_values = [10, 20, 30, 40, 50]
    calculator = AverageCalculator(sample_values)
    print(calculator.calculate_average())