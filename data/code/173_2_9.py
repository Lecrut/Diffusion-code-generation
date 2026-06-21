import pandas as pd

def group_and_mean(df, group_cols, mean_cols):
    return df.groupby(group_cols)[mean_cols].mean().reset_index()

if __name__ == '__main__':
    data = {
        'id': [1, 2, 3, 4, 5],
        'category': ['A', 'B', 'A', 'C', 'B'],
        'value': [10, 20, 15, 25, 30]
    }
    df = pd.DataFrame(data)
    result = group_and_mean(df, ['category'], ['value'])
    print(result)