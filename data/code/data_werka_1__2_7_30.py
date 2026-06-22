import pandas as pd

def scale_volumes(input_csv, output_csv, scale_factor):
    df = pd.read_csv(input_csv)
    df['Volume'] = df['Volume'] * scale_factor
    df.to_csv(output_csv, index=False)
if __name__ == '__main__':
    sample_data = 'ItemName,Volume\n    ItemA,10\n    ItemB,20\n    ItemC,30'
    with open('sample.csv', 'w') as f:
        f.write(sample_data)
    scale_factor = 2
    scale_volumes('sample.csv', 'output.csv', scale_factor)