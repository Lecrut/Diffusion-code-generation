import statistics

class DataAnalyzer:
    @staticmethod
    def calculate_stats(numbers):
        mean = statistics.mean(numbers)
        median = statistics.median(numbers)
        std_dev = statistics.stdev(numbers)
        return mean, median, std_dev

if __name__ == '__main__':
    sample_data = [10, 20, 30, 40, 50]
    analyzer = DataAnalyzer()
    mean, median, std_dev = analyzer.calculate_stats(sample_data)
    print(f"Mean: {mean}")
    print(f"Median: {median}")
    print(f"Standard Deviation: {std_dev}")