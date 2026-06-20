import tempfile
import os

def calculate_total_volume(filepath):
    total = 0.0
    with open(filepath, 'r') as f:
        for line in f:
            line = line.strip()
            if line:
                try:
                    volume = float(line)
                    total += volume
                except ValueError:
                    continue
    return total

if __name__ == '__main__':
    sample_lines = [
        "10.5",
        "20.3",
        "invalid",
        "5.2",
        "-3.1"
    ]
    
    fd, tmp_path = tempfile.mkstemp(suffix='.txt')
    try:
        with os.fdopen(fd, 'w') as f:
            for line in sample_lines:
                f.write(line + '\n')
        
        result = calculate_total_volume(tmp_path)
        print(result)
    finally:
        os.remove(tmp_path)