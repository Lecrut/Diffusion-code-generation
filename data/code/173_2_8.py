import pandas as pd

def group_and_mean(df, group_cols, mean_cols):
    return df.groupby(group_cols)[mean_cols].mean().reset_index()

if __name__ == '__main__':
    data = {
        'A': ['foo', 'bar', 'foo', 'bar', 'foo', 'bar', 'foo', 'foo'],
        'B': ['one', 'one', 'two', three, two, two, one, three],
        'C': [10, 20, 30, 40, 50, 60, 70, 80],
        'D': [100, 200, 300, 400, 500, 600, 700, 800]
    }
    df = pd.DataFrame(data)
    result = group_and_mean(df, ['A', 'B'], ['C', 'D'])
    print(result)