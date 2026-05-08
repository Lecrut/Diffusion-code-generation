class DataAnalyzer:
    def __init__(self, values):
        self.values = values
    def calculate_average(self):
        if not self.values:
            return 0
        return sum(self.values) / len(self.values)
if __name__ == '__main__':
    sample_data = [10, 20, 30, 40, 50]
    analyzer = DataAnalyzer(sample_data)
    average = analyzer.calculate_average()
    print(average)