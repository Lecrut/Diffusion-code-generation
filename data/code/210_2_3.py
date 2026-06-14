class DataAnalyzer:
    def calculate_range(self, data):
        if not data:
            return None
        return max(data) - min(data)
if __name__ == '__main__':
    analyzer = DataAnalyzer()
    sample_data = [10, 5, 20, 15, 8]
    range_value = analyzer.calculate_range(sample_data)
    print(range_value)