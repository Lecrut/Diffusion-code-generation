import pandas as pd

def scale_volumes(input_file_path, output_file_path, scale_factor):
    df = pd.read_csv(input_file_path)
    df['Volume'] *= scale_factor
    df.to_csv(output_file_path, index=False)
if __name__ == '__main__':
    input_data = 'Item,Volume\nApple,10\nBanana,20\nCherry,30'
    with open('temp_input.csv', 'w') as f:
        f.write(input_data)
    output_file_path = 'scaled_volumes.csv'
    scale_factor = 2
    scale_volumes('temp_input.csv', output_file_path, scale_factor)
    with open(output_file_path, 'r') as f:
        print(f.read())