import csv
import os
import tempfile
import statistics

def read_and_average_temperatures(file_path):
    temperatures = []
    try:
        with open(file_path, mode='r', newline='', encoding='utf-8') as file:
            reader = csv.reader(file)
            for row in reader:
                if len(row) >= 1 and row[0].strip():
                    try:
                        value = float(row[0].strip())
                        temperatures.append(value)
                    except ValueError:
                        continue
        if not temperatures:
            return 0.0
        return statistics.mean(temperatures)
    except FileNotFoundError:
        raise FileNotFoundError(f"File not found: {file_path}")
    except PermissionError:
        raise PermissionError(f"Permission denied: {file_path}")
    except csv.Error as e:
        raise RuntimeError(f"CSV parsing error: {e}")

if __name__ == '__main__':
    sample_content = "20.5\n21.3\n19.8\n22.1\n20.0"
    temp_file_path = os.path.join(tempfile.gettempdir(), 'sample_temp_data.csv')
    with open(temp_file_path, 'w', encoding='utf-8') as f:
        f.write(sample_content)
    try:
        result = read_and_average_temperatures(temp_file_path)
        print(f"{result:.2f}")
    finally:
        if os.path.exists(temp_file_path):
            os.remove(temp_file_path)