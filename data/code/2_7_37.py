import pandas as pd

def scale_volumes(input_file, output_file, scale_factor):
    df = pd.read_csv(input_file)
    df['Volume'] *= scale_factor
    df.to_csv(output_file, index=False)
if __name__ == '__main__':
    sample_data = 'ItemName,Volume\nItem1,10\nItem2,20\nItem3,30'
    import tempfile
    temp_file_in = tempfile.NamedTemporaryFile(delete=False)
    temp_file_out = tempfile.NamedTemporaryFile(delete=False, suffix='.csv')
    temp_file_in.write(sample_data.encode())
    temp_file_in.close()
    scale_volumes(temp_file_in.name, temp_file_out.name, 2)
    with open(temp_file_out.name, 'r') as f:
        print(f.read())
    import os
    os.remove(temp_file_in.name)
    os.remove(temp_file_out.name)