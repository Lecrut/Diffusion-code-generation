import pandas as pd

def average_of_pairs(df_column):
    return df_column.apply(lambda x: (x[0] + x[1]) / 2)

if __name__ == '__main__':
    sample_data = [([10, 5], 'A'), ([20, 8], 'B'), ([30, 12], 'C')]
    df = pd.DataFrame(sample_data, columns=['pair', 'category'])
    averages = average_of_pairs(df['pair'])
    print(averages)