import csv
import os
import tempfile

def calculate_average_temperature(file_path: str) -> float:
    temperatures = []
    with open(file_path, mode='r', newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        if not reader.fieldnames:
            raise ValueError('CSV file is empty or has no headers')
        temp_column = None
        if 'temperature' in reader.fieldnames:
            temp_column = 'temperature'
        else:
            for field in reader.fieldnames:
                try:
                    next(csv.DictReader(csvfile))
                    break
                except StopIteration:
                    continue
            csvfile.seek(0)
            reader = csv.DictReader(csvfile)
            for field in reader.fieldnames:
                try:
                    next_row = next(reader)
                    float(next_row[field])
                    temp_column = field
                    break
                except (ValueError, KeyError):
                    continue
                finally:
                    csvfile.seek(0)
                    reader = csv.DictReader(csvfile)
                    break
            if temp_column is None:
                raise ValueError('No valid temperature column found in CSV')
        for row in reader:
            try:
                temp = float(row[temp_column])
                temperatures.append(temp)
            except (ValueError, KeyError, TypeError):
                continue
    if not temperatures:
        raise ValueError('No valid temperature readings found in CSV')
    return sum(temperatures) / len(temperatures)

def create_sample_csv():
    fd, path = tempfile.mkstemp(suffix='.csv')
    try:
        with os.fdopen(fd, 'w', newline='') as f:
            writer = csv.writer(f)
            writer.writerow(['date', 'temperature', 'humidity'])
            writer.writerow(['2023-01-01', '20.5', '45'])
            writer.writerow(['2023-01-02', '22.3', '50'])
            writer.writerow(['2023-01-03', '18.7', '55'])
            writer.writerow(['2023-01-04', '25.1', '40'])
            writer.writerow(['2023-01-05', '19.9', '60'])
    except Exception:
        if os.path.exists(path):
            os.remove(path)
        raise
    return path
if __name__ == '__main__':
    sample_file = create_sample_csv()
    try:
        avg_temp = calculate_average_temperature(sample_file)
        print(avg_temp)
    finally:
        if os.path.exists(sample_file):
            os.remove(sample_file)