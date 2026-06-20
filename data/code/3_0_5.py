import csv
import io
import os

def calculate_average_temperature(file_path):
    temperatures = []
    with open(file_path, 'r', newline='') as csvfile:
        reader = csv.reader(csvfile)
        header = next(reader, None)
        if header is None:
            return None
        if not header:
            return None
        temp_idx = None
        for idx, col in enumerate(header):
            if col.lower().strip() in ['temperature', 'temp', 'celsius', 'fahrenheit']:
                temp_idx = idx
                break
        if temp_idx is None:
            raise ValueError("No temperature column found in CSV header")
        for row in reader:
            if not row:
                continue
            if len(row) <= temp_idx:
                continue
            val_str = row[temp_idx].strip()
            if not val_str:
                continue
            try:
                temp = float(val_str)
                temperatures.append(temp)
            except ValueError:
                continue
    if not temperatures:
        return None
    return sum(temperatures) / len(temperatures)

if __name__ == '__main__':
    temp_data = "timestamp,temperature,humidity\n2023-01-01 10:00,22.5,45\n2023-01-01 11:00,23.1,44\n2023-01-01 12:00,24.0,43\n2023-01-01 13:00,25.2,42"
    sample_csv_path = 'sample_temps.csv'
    with open(sample_csv_path, 'w', newline='') as f:
        f.write(temp_data)
    avg_temp = calculate_average_temperature(sample_csv_path)
    print(avg_temp)
    os.remove(sample_csv_path)