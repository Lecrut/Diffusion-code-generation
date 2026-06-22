class MeanCalculator:
    def __init__(self, numbers):
        self.numbers = numbers

    def calculate_mean(self):
        if not self.numbers:
            return 0
        return sum(self.numbers) / len(self.numbers)

if __name__ == '__main__':
    calculator = MeanCalculator([1.5, 2.5, 3.5])
    mean_value = calculator.calculate_mean()
    print(f"Mean of [1.5, 2.5, 3.5]: {mean_value}")