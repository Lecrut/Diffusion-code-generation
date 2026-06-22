import pandas as pd

class DataFrameAnalyzer:
    def __init__(self, data):
        self.df = pd.DataFrame(data)
    
    def find_min_max(self, column_name):
        return {
            'smallest': self.df[column_name].min(),
            'largest': self.df[column_name].max()
        }

if __name__ == '__main__':
    sample_data = {'numbers': [15, 3, 8, 22, 1]}
    analyzer = DataFrameAnalyzer(sample_data)
    result = analyzer.find_min_max('numbers')
    print(result)