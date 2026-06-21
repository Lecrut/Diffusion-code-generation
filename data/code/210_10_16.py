class DataAnalyzer:
    def __init__(self, data):
        self.data = data

    def calculate_range(self):
        return max(self.data) - min(self.data)

if __name__ == '__main__':
    sample_values = [34, 12, 90, 56, 23]
    analyzer = DataAnalyzer(sample_values)
    print(analyzer.calculate_range())