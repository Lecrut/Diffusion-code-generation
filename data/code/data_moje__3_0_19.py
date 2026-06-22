import csv
import tempfile
import os

def calculate_average_temperature(csv_file_path):
    try:
        with open(csv_file_path, 'r', newline='') as file:
            reader = csv.reader(file)
            header = next(reader, None)
            if header is None:
                return None
            temperature_index = None
            for idx, col_name in enumerate(header):
                if 'temperature' in col_name.lower():
                    temperature_index = idx
                    break
            if temperature_index is None:
                return None
            temperatures = []
            for row in reader:
                if len(row) > temperature_index:
                    try:
                        temp_value = float(row[temperature_index])
                        temperatures.append(temp_value)
                    except ValueError:
                        continue
            if not temperatures:
                return None
            average = sum(temperatures) / len(temperatures)
            return average
    except FileNotFoundError:
        return None
    except Exception:
        return None
if __name__ == '__main__':
    sample_csv_content = 'Date,Time,Temperature,Humidity\n2023-01-01,00:00,22.5,45.0\n2023-01-01,01:00,22.1,46.0\n2023-01-01,02:00,21.8,47.0\n2023-01-01,03:00,21.5,48.0\n2023-01-01,04:00,21.2,49.0\n'
    tmp_file = tempfile.NamedTemporaryFile(mode='w', suffix='.csv', delete=False)
    tmp_file.write(sample_csv_content)
    tmp_file.close()
    try:
        result = calculate_average_temperature(tmp_file.name)
        print(result)
    finally:
        os.unlink(tmp_file.name)