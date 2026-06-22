import csv
import tempfile
import os

def calculate_average_temperature(filepath):
    try:
        with open(filepath, 'r', newline='') as csvfile:
            reader = csv.DictReader(csvfile)
            temperatures = []
            for row in reader:
                try:
                    temp = float(row['temperature'])
                    temperatures.append(temp)
                except (KeyError, ValueError):
                    continue
            if not temperatures:
                return None
            return sum(temperatures) / len(temperatures)
    except FileNotFoundError:
        raise FileNotFoundError(f"The file {filepath} was not found.")
    except Exception as e:
        raise e

def create_sample_csv():
    fd, temp_path = tempfile.mkstemp(suffix='.csv')
    with os.fdopen(fd, 'w', newline='') as f:
        writer = csv.writer(f)
        writer.writerow(['timestamp', 'temperature', 'humidity'])
        writer.writerow(['2023-10-01 00:00:00', '22.5', '45'])
        writer.writerow(['2023-10-01 01:00:00', '21.8', '46'])
        writer.writerow(['2023-10-01 02:00:00', '23.1', '44'])
    return temp_path

if __name__ == '__main__':
    sample_file = create_sample_csv()
    average = calculate_average_temperature(sample_file)
    print(average)
    os.remove(sample_file)