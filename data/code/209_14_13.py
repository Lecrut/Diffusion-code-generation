class MeanCalculator:
    DEFAULT_SAMPLES = [10, 20, 30, 40, 50]

    @staticmethod
    def calculate_mean(samples):
        if not samples:
            raise ValueError("Input list cannot be empty")
        return sum(samples) / len(samples)

if __name__ == '__main__':
    calculator = MeanCalculator()
    test_samples = MeanCalculator.DEFAULT_SAMPLES
    print(calculator.calculate_mean(test_samples))