import pandas as pd

def scale_volumes(input_csv, output_csv, scale_factor):
    df = pd.read_csv(input_csv)
    df['Volume'] *= scale_factor
    df.to_csv(output_csv, index=False)
if __name__ == '__main__':
    sample_data = 'ItemName,Volume\nApple,10\nBanana,20\nCherry,30'
    with open('sample.csv', 'w') as f:
        f.write(sample_data)
    scale_factor = 1.5
    scale_volumes('sample.csv', 'output.csv', scale_factor)
    with open('output.csv', 'r') as f:
        print(f.read())