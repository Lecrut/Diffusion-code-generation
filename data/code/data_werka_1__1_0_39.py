import pandas as pd

def calculate_average_weights(file_path):
    df = pd.read_csv(file_path)
    average_weights = df.groupby('category')['weight'].mean().reset_index()
    return average_weights
if __name__ == '__main__':
    sample_csv_content = 'category,weight\nfruits,150\nvegetables,200\nfruits,170\ngrains,50\nvegetables,210'
    with open('sample_weights.csv', 'w') as f:
        f.write(sample_csv_content)
    result = calculate_average_weights('sample_weights.csv')
    print(result)