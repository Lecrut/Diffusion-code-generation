import pandas as pd

def scale_volumes(input_file, output_file, factor):
    df = pd.read_csv(input_file)
    df['Volume'] *= factor
    df.to_csv(output_file, index=False)
if __name__ == '__main__':
    input_data = 'Item,Volume\nItem1,10\nItem2,20\nItem3,30'
    output_file = 'scaled_volumes.csv'
    scale_factor = 2.5
    with open('temp_input.csv', 'w') as f:
        f.write(input_data)
    scale_volumes('temp_input.csv', output_file, scale_factor)
    with open(output_file, 'r') as f:
        print(f.read())