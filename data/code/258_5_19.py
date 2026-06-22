import pandas as pd

class AveragePairs:
    def __init__(self):
        self.data = None

    def calculate_averages(self, df, column_name):
        if not isinstance(df, pd.DataFrame) or column_name not in df.columns:
            raise ValueError("Invalid DataFrame or column name")
        
        self.data = df[column_name].apply(lambda x: sum(x) / len(x))
        return self.data

if __name__ == '__main__':
    sample_data = {
        'pairs': [(10, 5), (20, 8), (30, 12)]
    }
    df = pd.DataFrame(sample_data)
    
    avg_pairs = AveragePairs()
    averages = avg_pairs.calculate_averages(df, 'pairs')
    
    print(averages)