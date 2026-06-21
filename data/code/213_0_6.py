import statistics

class DataAnalyzer:
    def __init__(self, data):
        self.data = data
    
    def calculate_mean(self):
        return statistics.mean(self.data)
    
    def calculate_median(self):
        return statistics.median(self.data)
    
    def calculate_std_dev(self):
        return statistics.stdev(self.data)

if __name__ == '__main__':
    sample_data = [10, 20, 30, 40, 50]
    analyzer = DataAnalyzer(sample_data)
    print(f"Mean: {analyzer.calculate_mean()}")
    print(f"Median: {analyzer.calculate_median()}")
    print(f"Standard Deviation: {analyzer.calculate_std_dev()}")