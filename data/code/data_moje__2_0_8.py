import csv
import tempfile
import os

def calculate_total_volume_from_file(filepath):
    total_volume = 0.0
    try:
        with open(filepath, 'r') as f:
            reader = csv.reader(f)
            for row in reader:
                if not row:
                    continue
                try:
                    volume_value = float(row[0])
                    total_volume += volume_value
                except (ValueError, IndexError):
                    continue
    except FileNotFoundError:
        raise FileNotFoundError(f"The file {filepath} was not found.")
    except PermissionError:
        raise PermissionError(f"Permission denied to read {filepath}.")
    except IOError as e:
        raise IOError(f"An error occurred while reading the file: {e}")
    return total_volume

if __name__ == '__main__':
    sample_data = [
        "10.5",
        "20.3",
        "invalid",
        "5.2"
    ]
    
    with tempfile.NamedTemporaryFile(mode='w', suffix='.csv', delete=False) as tmp_file:
        for line in sample_data:
            tmp_file.write(line + '\n')
        temp_filepath = tmp_file.name
    
    try:
        total = calculate_total_volume_from_file(temp_filepath)
        print(total)
    finally:
        os.unlink(temp_filepath)