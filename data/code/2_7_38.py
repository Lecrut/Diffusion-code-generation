import pandas as pd

def scale_volumes(input_csv, output_csv, scale_factor):
    df = pd.read_csv(input_csv)
    df['Volume'] *= scale_factor
    df.to_csv(output_csv, index=False)

if __name__ == '__main__':
    input_data = """ItemName,Volume
Apple,10
Banana,20
Cherry,30"""
    
    with open('input.csv', 'w') as f:
        f.write(input_data)
    
    scale_factor = 2
    output_csv = 'output.csv'
    
    scale_volumes('input.csv', output_csv, scale_factor)
    
    result_df = pd.read_csv(output_csv)
    print(result_df)