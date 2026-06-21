import statistics

class DataAnalyzer:
    SAMPLE_DATA = [10, 25, 32, 8, 45]

    @staticmethod
    def calculate_mean(data):
        return sum(data) / len(data) if data else 0

    @staticmethod
    def calculate_median(data):
        return statistics.median(data)

    @staticmethod
    def calculate_std_deviation(data):
        return statistics.stdev(data) if len(data) > 1 else 0

if __name__ == '__main__':
    analyzer = DataAnalyzer()
    mean_value = analyzer.calculate_mean(DataAnalyzer.SAMPLE_DATA)
    median_value = analyzer.calculate_median(DataAnalyzer.SAMPLE_DATA)
    std_dev_value = analyzer.calculate_std_deviation(DataAnalyzer.SAMPLE_DATA)

    print(f"List: {DataAnalyzer.SAMPLE_DATA}")
    print(f"Mean: {mean_value}")
    print(f"Median: {median_value}")
    print(f"Standard Deviation: {std_dev_value}")