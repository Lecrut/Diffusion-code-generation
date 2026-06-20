import os
import tempfile

def read_volume_file(filepath):
    if not os.path.exists(filepath):
        raise FileNotFoundError(f'The file {filepath} does not exist.')
    volumes = []
    with open(filepath, 'r') as f:
        for line_num, line in enumerate(f, 1):
            line = line.strip()
            if not line:
                continue
            try:
                volume = float(line)
                volumes.append(volume)
            except ValueError:
                raise ValueError(f"Non-numeric value '{line}' found at line {line_num}.")
    return volumes

def calculate_total_volume(filepath):
    volumes = read_volume_file(filepath)
    return sum(volumes)

def create_sample_volume_file():
    sample_data = ['10.5', '20.0', '30.5', '0', '-5.0']
    with tempfile.NamedTemporaryFile(mode='w', suffix='.txt', delete=False) as f:
        for volume in sample_data:
            f.write(volume + '\n')
        temp_path = f.name
    return temp_path
if __name__ == '__main__':
    temp_file_path = create_sample_volume_file()
    try:
        total = calculate_total_volume(temp_file_path)
        print(total)
    finally:
        os.unlink(temp_file_path)