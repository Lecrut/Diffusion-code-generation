import csv
import os
import tempfile

def calculate_average_temperature(csv_path):
    try:
        with open(csv_path, 'r', newline='') as file:
            reader = csv.DictReader(file)
            total = 0
            count = 0
            for row in reader:
                if 'temperature' in row:
                    try:
                        temp_value = float(row['temperature'])
                        total += temp_value
                        count += 1
                    except ValueError:
                        continue
            if count == 0:
                return 0.0
            return total / count
    except FileNotFoundError:
        raise FileNotFoundError(f"File not found: {csv_path}")
    except Exception as e:
        raise RuntimeError(f"Error reading file: {e}")

if __name__ == '__main__':
    sample_data = "timestamp,temperature\n2023-01-01 00:00:00,20.5\n2023-01-01 01:00:00,22.0\n2023-01-01 02:00:00,19.5\n2023-01-01 03:00:00,21.0"
    
    with tempfile.NamedTemporaryFile(mode='w', delete=False, suffix='.csv') as tmpfile:
        tmpfile.write(sample_data)
        tmpfile_path = tmpfile.name
    
    try:
        result = calculate_average_temperature(tmpfile_path)
        print(result)
    finally:
        if os.path.exists(tmpfile_path):
            os.remove(tmpfile_path)