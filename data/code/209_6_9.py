class AverageCalculator:
    def __init__(self, samples):
        self.samples = samples

    def calculate_average(self):
        if not self.samples:
            return 0
        return sum(self.samples) / len(self.samples)

if __name__ == '__main__':
    calculator = AverageCalculator([12, 24, 36])
    average = calculator.calculate_average()
    print(f"The average is: {average}")