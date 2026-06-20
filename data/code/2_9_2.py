import os
import tempfile

def calculate_total_volume(file_path):
    total = 0.0
    try:
        with open(file_path, 'r') as f:
            for line in f:
                line = line.strip()
                if not line:
                    continue
                try:
                    value = float(line)
                    total += value
                except ValueError:
                    continue
        return total
    except FileNotFoundError:
        return 0.0
    except IOError:
        return 0.0

if __name__ == '__main__':
    sample_data = ["10.5", "20.3", "invalid", "5.0", "error", "14.2"]
    with tempfile.NamedTemporaryFile(mode='w', delete=False, suffix='.txt') as temp_file:
        temp_path = temp_file.name
        for item in sample_data:
            temp_file.write(item + '\n')
    
    result = calculate_total_volume(temp_path)
    print(f"{result}")
    
    os.remove(temp_path)