import pandas as pd

def calculate_average_weights(file_path):
    df = pd.read_csv(file_path)
    average_weights = df.groupby('category')['weight'].mean()
    return average_weights
if __name__ == '__main__':
    sample_data = 'category,weight\napple,150\nbanana,120\napple,160\norange,130\nbanana,110'
    with open('sample_weights.csv', 'w') as f:
        f.write(sample_data)
    result = calculate_average_weights('sample_weights.csv')
    print(result)