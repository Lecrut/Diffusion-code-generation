import pandas as pd

def scale_volumes(input_file_path, output_file_path, scale_factor):
    df = pd.read_csv(input_file_path)
    df['Volume'] *= scale_factor
    df.to_csv(output_file_path, index=False)
if __name__ == '__main__':
    sample_data = {'Item': ['Item1', 'Item2', 'Item3'], 'Volume': [10, 20, 30]}
    import tempfile
    import os
    temp_dir = tempfile.mkdtemp()
    input_file_path = os.path.join(temp_dir, 'input.csv')
    output_file_path = os.path.join(temp_dir, 'output.csv')
    pd.DataFrame(sample_data).to_csv(input_file_path, index=False)
    scale_factor = 2
    scale_volumes(input_file_path, output_file_path, scale_factor)
    result_df = pd.read_csv(output_file_path)
    print(result_df)