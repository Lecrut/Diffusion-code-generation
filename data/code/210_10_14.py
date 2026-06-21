class DataAnalyzer:
    @staticmethod
    def calculate_range(numbers):
        return max(numbers) - min(numbers)

if __name__ == '__main__':
    sample_values = [34, 12, 90, 56, 23]
    analyzer = DataAnalyzer()
    print(analyzer.calculate_range(sample_values))