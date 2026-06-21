class StatisticsCalculator:
    @staticmethod
    def calculate_mean(samples):
        if not samples:
            raise ValueError("Input list cannot be empty")
        return sum(samples) / len(samples)

if __name__ == '__main__':
    test_samples = [10, 20, 30, 40, 50]
    calculator = StatisticsCalculator()
    mean_value = calculator.calculate_mean(test_samples)
    print(mean_value)