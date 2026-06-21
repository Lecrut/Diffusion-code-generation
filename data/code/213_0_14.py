import statistics

class StatsCalculator:
    def __init__(self, numbers):
        self.numbers = numbers

    @staticmethod
    def calculate_mean(numbers):
        return statistics.mean(numbers)

    @staticmethod
    def calculate_median(numbers):
        return statistics.median(numbers)

    @staticmethod
    def calculate_std_dev(numbers):
        return statistics.stdev(numbers)

if __name__ == '__main__':
    sample_numbers = [10, 20, 30, 40, 50]
    calculator = StatsCalculator(sample_numbers)
    mean = calculator.calculate_mean(calculator.numbers)
    median = calculator.calculate_median(calculator.numbers)
    std_dev = calculator.calculate_std_dev(calculator.numbers)
    print(f"Mean: {mean}")
    print(f"Median: {median}")
    print(f"Standard Deviation: {std_dev}")