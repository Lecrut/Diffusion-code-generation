import csv
import os
import tempfile

def calculate_average_temperature(file_path):
    try:
        with open(file_path, 'r', newline='') as csvfile:
            reader = csv.DictReader(csvfile)
            temperatures = []
            for row in reader:
                if 'temperature' in row and row['temperature']:
                    temp_value = float(row['temperature'])
                    temperatures.append(temp_value)
            if not temperatures:
                return 0.0
            return sum(temperatures) / len(temperatures)
    except FileNotFoundError:
        raise FileNotFoundError(f"The file {file_path} was not found.")
    except ValueError as e:
        raise ValueError(f"Invalid temperature value in file: {e}")
    except Exception as e:
        raise Exception(f"An error occurred while processing the file: {e}")

if __name__ == '__main__':
    sample_data = """timestamp,temperature
2023-01-01 08:00:00,20.5
2023-01-01 09:00:00,22.3
2023-01-01 10:00:00,21.0
2023-01-01 11:00:00,19.8
2023-01-01 12:00:00,23.4"""
    
    with tempfile.NamedTemporaryFile(mode='w', delete=False, suffix='.csv', newline='') as tmpfile:
        tmpfile.write(sample_data)
        temp_file_path = tmpfile.name

    try:
        average_temp = calculate_average_temperature(temp_file_path)
        print(f"Average Temperature: {average_temp:.2f}")
    finally:
        os.remove(temp_file_path)