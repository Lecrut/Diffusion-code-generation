import tempfile
import os

def calculate_total_volume(file_path):
    total = 0.0
    with open(file_path, 'r') as f:
        for line in f:
            line = line.strip()
            if not line:
                continue
            try:
                volume = float(line)
                total += volume
            except ValueError:
                continue
    return total

if __name__ == '__main__':
    sample_data = """10.5
20.0
30.25
bad_value
40.0"""

    with tempfile.NamedTemporaryFile(mode='w', delete=False, suffix='.txt') as f:
        f.write(sample_data)
        temp_file_path = f.name

    try:
        result = calculate_total_volume(temp_file_path)
        print(result)
    finally:
        os.unlink(temp_file_path)