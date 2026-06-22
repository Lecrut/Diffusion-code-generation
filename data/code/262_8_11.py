import pandas as pd

class DataAnalyzer:
    @staticmethod
    def find_min_max(data_frame, column_name):
        return {
            'smallest': data_frame[column_name].min(),
            'largest': data_frame[column_name].max()
        }

if __name__ == '__main__':
    sample_data = {'values': [15, 3, 8, 22, 1]}
    df = pd.DataFrame(sample_data)
    result = DataAnalyzer.find_min_max(df, 'values')
    print(result)