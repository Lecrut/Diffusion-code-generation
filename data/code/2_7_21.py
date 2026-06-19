import pandas as pd

def scale_volumes(input_csv, output_csv, factor):
    df = pd.read_csv(input_csv)
    df['Volume'] *= factor
    df.to_csv(output_csv, index=False)

if __name__ == '__main__':
    input_data = """Item,Volume\nApple,10\nBanana,20\nCherry,30"""
    with open('input.csv', 'w') as f:
        f.write(input_data)
    
    scale_volumes('input.csv', 'output.csv', 2)
    
    with open('output.csv', 'r') as f:
        print(f.read())