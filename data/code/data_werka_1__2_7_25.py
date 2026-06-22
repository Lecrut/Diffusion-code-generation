import pandas as pd

def scale_volumes(input_csv, output_csv, scale_factor):
    df = pd.read_csv(input_csv)
    df['Volume'] *= scale_factor
    df.to_csv(output_csv, index=False)
if __name__ == '__main__':
    sample_data = 'ItemName,Volume\nApple,10\nBanana,20\nCherry,30'
    with open('sample_input.csv', 'w') as f:
        f.write(sample_data)
    output_file = 'scaled_output.csv'
    scale_factor = 2
    scale_volumes('sample_input.csv', output_file, scale_factor)
    result_df = pd.read_csv(output_file)
    print(result_df)