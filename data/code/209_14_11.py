class MeanCalculator:
    def __init__(self):
        self.samples = []

    def add_sample(self, sample):
        if not isinstance(sample, (int, float)):
            raise ValueError("Sample must be an integer or float")
        self.samples.append(sample)

    def calculate_mean(self):
        if not self.samples:
            raise ValueError("Input list cannot be empty")
        return sum(self.samples) / len(self.samples)

if __name__ == '__main__':
    calculator = MeanCalculator()
    calculator.add_sample(10)
    calculator.add_sample(20)
    calculator.add_sample(30)
    calculator.add_sample(40)
    calculator.add_sample(50)
    print(calculator.calculate_mean())