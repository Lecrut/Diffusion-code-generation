class DataAnalyzer:
    def __init__(self, data):
        self.data = data

    def calculate_range(self):
        values = [self.data[key] for key in self.data]
        min_val = min(values)
        max_val = max(values)
        return max_val - min_val, [key for key in self.data if self.data[key] == min_val][0], [key for key in self.data if self.data[key] == max_val][0]

if __name__ == '__main__':
    sample_data = {
        'A': 10,
        'B': 20,
        'C': 5,
        'D': 30
    }
    analyzer = DataAnalyzer(sample_data)
    range_value, min_label, max_label = analyzer.calculate_range()
    print(f"Range: {range_value}, Min Label: {min_label}, Max Label: {max_label}")