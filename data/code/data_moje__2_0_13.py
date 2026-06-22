import os
import tempfile
import sys

def read_and_calculate_volume(file_path):
    total_volume = 0.0
    try:
        with open(file_path, 'r') as f:
            for line in f:
                line = line.strip()
                if not line:
                    continue
                try:
                    volume = float(line)
                    if volume < 0:
                        raise ValueError("Negative volume")
                    total_volume += volume
                except ValueError:
                    continue
    except FileNotFoundError:
        raise FileNotFoundError(f"The file {file_path} does not exist.")
    except IOError as e:
        raise IOError(f"Error reading file {file_path}: {e}")
    return total_volume

def create_sample_file(file_path, volumes):
    with open(file_path, 'w') as f:
        for v in volumes:
            f.write(f"{v}\n")

if __name__ == '__main__':
    sample_volumes = [10.5, 20.3, 5.2, -1.0, 15.0, "invalid", 25.5]
    
    temp_fd, temp_path = tempfile.mkstemp(suffix='.txt')
    os.close(temp_fd)
    
    try:
        create_sample_file(temp_path, sample_volumes)
        total = read_and_calculate_volume(temp_path)
        print(total)
    finally:
        if os.path.exists(temp_path):
            os.remove(temp_path)