import os
import tempfile

def calculate_total_volume(file_path):
    total_volume = 0.0
    try:
        with open(file_path, 'r') as f:
            for line in f:
                stripped = line.strip()
                if stripped:
                    try:
                        value = float(stripped)
                        total_volume += value
                    except ValueError:
                        continue
    except FileNotFoundError:
        raise FileNotFoundError(f"The file {file_path} was not found.")
    except PermissionError:
        raise PermissionError(f"Permission denied for {file_path}.")
    except IOError:
        raise IOError(f"An I/O error occurred while reading {file_path}.")
    return total_volume

def create_sample_file():
    temp_dir = tempfile.gettempdir()
    sample_path = os.path.join(temp_dir, 'volume_data.txt')
    sample_data = [10.5, 20.0, 3.14, 100.0, -5.5, 0]
    with open(sample_path, 'w') as f:
        for val in sample_data:
            f.write(f"{val}\n")
    return sample_path

if __name__ == '__main__':
    sample_file_path = create_sample_file()
    try:
        result = calculate_total_volume(sample_file_path)
        print(result)
    except (FileNotFoundError, PermissionError, IOError) as e:
        print(f"Error: {e}")
    finally:
        if os.path.exists(sample_file_path):
            os.remove(sample_file_path)