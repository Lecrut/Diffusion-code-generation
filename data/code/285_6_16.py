import pandas as pd

def compare_consecutive_elements(df, column_name):
    comparison_results = []
    for i in range(len(df) - 1):
        if df[column_name][i] < df[column_name][i + 1]:
            comparison_results.append('increasing')
        elif df[column_name][i] > df[column_name][i + 1]:
            comparison_results.append('decreasing')
        else:
            comparison_results.append('equal')
    comparison_results.append(None)
    return comparison_results
if __name__ == '__main__':
    data = {'values': [1, 2, 3, 4, 5]}
    df = pd.DataFrame(data)
    result = compare_consecutive_elements(df, 'values')
    print(result)