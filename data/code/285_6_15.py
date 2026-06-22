import pandas as pd

def compare_consecutive_elements(df, column_name):
    if not isinstance(df, pd.DataFrame) or column_name not in df.columns:
        raise ValueError("Invalid DataFrame or column name")
    
    result = []
    for i in range(len(df[column_name]) - 1):
        if df[column_name][i] < df[column_name][i + 1]:
            result.append('increasing')
        elif df[column_name][i] > df[column_name][i + 1]:
            result.append('decreasing')
        else:
            result.append('equal')
    
    return pd.Series(result, name=f'{column_name}_comparison')

if __name__ == '__main__':
    data = {'values': [10, 20, 30, 40, 50]}
    df = pd.DataFrame(data)
    comparison_result = compare_consecutive_elements(df, 'values')
    print(comparison_result)