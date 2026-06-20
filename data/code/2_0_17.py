import os
import sys

def read_volumes_from_file(filepath):
    if not os.path.exists(filepath):
        raise FileNotFoundError(f"The file {filepath} does not exist")
    volumes = []
    try:
        with open(filepath, 'r') as f:
            for line in f:
                line = line.strip()
                if not line:
                    continue
                try:
                    value = float(line)
                    if value < 0:
                        raise ValueError(f"Negative volume {value} found on line: {line}")
                    volumes.append(value)
                except ValueError:
                    raise ValueError(f"Invalid volume format '{line}' on line: {line}")
    except PermissionError:
        raise PermissionError(f"Permission denied reading file: {filepath}")
    except IOError as e:
        raise IOError(f"IO error while reading file: {filepath}, details: {e}")
    return volumes

def calculate_total_volume(filepath):
    volumes = read_volumes_from_file(filepath)
    return sum(volumes)

def create_sample_file(filename, content):
    with open(filename, 'w') as f:
        for value in content:
            f.write(f"{value}\n")

if __name__ == '__main__':
    sample_filename = 'sample_volumes.txt'
    sample_data = [10.5, 20.3, 5.0, 15.2]
    create_sample_file(sample_filename, sample_data)
    total = calculate_total_volume(sample_filename)
    print(total)
    os.remove(sample_filename)