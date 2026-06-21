import pandas as pd

class DataAnalyzer:
    def __init__(self, data):
        self.df = pd.DataFrame(data)
    
    def preprocess_data(self):
        self.df['value'] = self.df['value'].fillna(0)
    
    def calculate_means(self):
        return self.df.groupby('category')['value'].mean().reset_index()

if __name__ == '__main__':
    sample_data = {
        'category': ['A', 'B', 'A', 'C', 'B', 'A'],
        'value': [10, 20, None, 30, 40, 50]
    }
    
    analyzer = DataAnalyzer(sample_data)
    analyzer.preprocess_data()
    result = analyzer.calculate_means()
    print(result)