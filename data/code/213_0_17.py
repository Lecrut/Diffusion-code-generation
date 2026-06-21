import statistics

class StatsCalculator:
    def __init__(self, numbers):
        self.numbers = numbers
    
    def calculate_mean(self):
        return statistics.mean(self.numbers)
    
    def calculate_median(self):
        return statistics.median(self.numbers)
    
    def calculate_std_dev(self):
        return statistics.stdev(self.numbers)

if __name__ == '__main__':
    sample_numbers = [10, 20, 30, 40, 50]
    calculator = StatsCalculator(sample_numbers)
    mean = calculator.calculate_mean()
    median = calculator.calculate_median()
    std_dev = calculator.calculate_std_dev()
    
    print(f"Mean: {mean}")
    print(f"Median: {median}")
    print(f"Standard Deviation: {std_dev}")