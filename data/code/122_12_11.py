class NumberCalculator:
    def __init__(self, values):
        self.values = values

    def calculate_mean(self):
        return sum(self.values) / len(self.values)

if __name__ == '__main__':
    sample_numbers = [10, 20, 30, 40, 50]
    calculator = NumberCalculator(sample_numbers)
    mean_value = calculator.calculate_mean()
    print(mean_value)