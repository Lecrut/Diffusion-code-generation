import pandas as pd

class DataAnalyzer:
    def __init__(self, data):
        self.data = data

    def find_extremes(self):
        if not self.data.empty and 'numerical_column' in self.data.columns:
            min_value = self.data['numerical_column'].min()
            max_value = self.data['numerical_column'].max()
            return {'smallest': min_value, 'largest': max_value}
        else:
            return None

if __name__ == '__main__':
    sample_data = {
        'numerical_column': [15, 3, 8, 22, 1]
    }
    df = pd.DataFrame(sample_data)
    analyzer = DataAnalyzer(df)
    result = analyzer.find_extremes()
    print(result)