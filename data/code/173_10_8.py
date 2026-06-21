import pandas as pd

class DataAnalyzer:
    CATEGORY_COLUMN = 'category'
    VALUE_COLUMN = 'value'

    @staticmethod
    def calculate_category_means(data):
        df = pd.DataFrame(data)
        df[DataAnalyzer.VALUE_COLUMN] = df[DataAnalyzer.VALUE_COLUMN].fillna(0)
        result = df.groupby(DataAnalyzer.CATEGORY_COLUMN)[DataAnalyzer.VALUE_COLUMN].mean().reset_index()
        return result

if __name__ == '__main__':
    sample_data = {'category': ['A', 'B', 'A', 'C', 'B', 'A'], 'value': [10, 20, None, 30, 40, 50]}
    analyzer = DataAnalyzer()
    result = analyzer.calculate_category_means(sample_data)
    print(result)