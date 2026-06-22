class DataAnalyzer:
    def __init__(self, data):
        self.data = data

    def calculate_range(self):
        values = list(self.data.values())
        min_val = min(values)
        max_val = max(values)
        return max_val - min_val

if __name__ == '__main__':
    sample_data = {
        'A': 10,
        'B': 20,
        'C': 5,
        'D': 30
    }
    analyzer = DataAnalyzer(sample_data)
    range_value = analyzer.calculate_range()
    print(f"Range: {range_value}")