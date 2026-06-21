class DataAnalyzer:
    def __init__(self, numbers):
        self.numbers = numbers

    def calculate_range(self):
        return max(self.numbers) - min(self.numbers)

if __name__ == '__main__':
    sample_values = [34, 12, 90, 56, 23]
    analyzer = DataAnalyzer(sample_values)
    print(analyzer.calculate_range())