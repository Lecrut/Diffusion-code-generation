import csv
import os

def calculate_average_temperature(file_path):
    if not os.path.exists(file_path):
        raise FileNotFoundError(f"The file {file_path} does not exist")
    
    temperatures = []
    with open(file_path, 'r', newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            try:
                temp_value = float(row['temperature'])
                temperatures.append(temp_value)
            except (KeyError, ValueError):
                continue
    
    if not temperatures:
        raise ValueError("No valid temperature readings found in the file")
    
    return sum(temperatures) / len(temperatures)

def create_sample_csv():
    sample_data = [
        {'timestamp': '2023-01-01 00:00', 'temperature': '20.5'},
        {'timestamp': '2023-01-01 01:00', 'temperature': '21.0'},
        {'timestamp': '2023-01-01 02:00', 'temperature': '19.5'},
        {'timestamp': '2023-01-01 03:00', 'temperature': '22.0'},
        {'timestamp': '2023-01-01 04:00', 'temperature': 'invalid'},
        {'timestamp': '2023-01-01 05:00', 'temperature': '21.5'}
    ]
    filename = 'sample_temperatures.csv'
    with open(filename, 'w', newline='') as csvfile:
        fieldnames = ['timestamp', 'temperature']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()
        for row in sample_data:
            writer.writerow(row)
    return filename

if __name__ == '__main__':
    csv_filename = create_sample_csv()
    try:
        avg_temp = calculate_average_temperature(csv_filename)
        print(f"Average temperature: {avg_temp}")
    except FileNotFoundError as e:
        print(f"File error: {e}")
    except ValueError as e:
        print(f"Data error: {e}")