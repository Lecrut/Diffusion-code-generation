import pandas as pd

def scale_volumes(input_file, output_file, factor):
    df = pd.read_csv(input_file)
    df['Volume'] *= factor
    df.to_csv(output_file, index=False)
if __name__ == '__main__':
    sample_data = 'ItemName,Volume\nApple,10\nBanana,20\nCherry,30'
    input_file = 'input.csv'
    with open(input_file, 'w') as f:
        f.write(sample_data)
    output_file = 'output.csv'
    scale_factor = 1.5
    scale_volumes(input_file, output_file, scale_factor)
    with open(output_file, 'r') as f:
        print(f.read())