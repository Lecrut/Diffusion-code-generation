import pandas as pd

class DataAnalyzer:
    def __init__(self, data):
        self.data = data

    def find_range(self):
        if self.data.empty:
            return None
        min_val = self.data.min()
        max_val = self.data.max()
        return max_val - min_val

if __name__ == '__main__':
    sample_data = pd.DataFrame({'values': [3.14, 1.618, 2.718, 0.577, 9.999, -10.0, 5.0]})
    analyzer = DataAnalyzer(sample_data['values'])
    result = analyzer.find_range()
    print(result)