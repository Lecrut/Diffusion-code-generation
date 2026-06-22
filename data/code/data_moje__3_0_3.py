import csv
import os
import tempfile

def calculate_average_temperature(file_path: str) -> float:
    if not os.path.exists(file_path):
        raise FileNotFoundError(f'The file {file_path} does not exist.')
    temperatures = []
    try:
        with open(file_path, mode='r', newline='') as csvfile:
            reader = csv.DictReader(csvfile)
            if 'temperature' not in reader.fieldnames:
                raise ValueError("CSV file must contain a 'temperature' column.")
            for row in reader:
                try:
                    temp_value = float(row['temperature'])
                    temperatures.append(temp_value)
                except (ValueError, TypeError):
                    continue
    except IOError as e:
        raise IOError(f'Error reading file: {e}')
    if not temperatures:
        raise ValueError('No valid temperature readings found in the file.')
    return sum(temperatures) / len(temperatures)

def main():
    data_content = 'temperature\n20.5\n22.0\n19.5\n21.0'
    with tempfile.NamedTemporaryFile(mode='w', suffix='.csv', delete=False) as f:
        f.write(data_content)
        temp_file_name = f.name
    try:
        avg_temp = calculate_average_temperature(temp_file_name)
        print(avg_temp)
    finally:
        os.unlink(temp_file_name)
if __name__ == '__main__':
    main()