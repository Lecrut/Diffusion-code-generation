import csv
import os
import tempfile

def calculate_average_temperature(csv_file_path):
    if not os.path.exists(csv_file_path):
        raise FileNotFoundError(f"The file {csv_file_path} does not exist.")
    
    temperatures = []
    try:
        with open(csv_file_path, 'r') as file:
            reader = csv.reader(file)
            header = next(reader, None)
            if header is None:
                raise ValueError("The CSV file is empty.")
            
            temp_col_index = None
            for i, col_name in enumerate(header):
                if col_name.strip().lower() == 'temperature':
                    temp_col_index = i
                    break
            
            if temp_col_index is None:
                raise ValueError("The CSV file does not contain a 'temperature' column.")
            
            for row in reader:
                if len(row) > temp_col_index:
                    try:
                        temp_value = float(row[temp_col_index])
                        temperatures.append(temp_value)
                    except ValueError:
                        continue
    except IOError as e:
        raise IOError(f"Error reading file: {e}")
    
    if not temperatures:
        return 0.0
    
    return sum(temperatures) / len(temperatures)

def create_sample_csv(file_path):
    with open(file_path, 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(['date', 'temperature', 'humidity'])
        writer.writerow(['2023-10-01', '22.5', '60'])
        writer.writerow(['2023-10-02', '23.1', '55'])
        writer.writerow(['2023-10-03', '21.8', '65'])
        writer.writerow(['2023-10-04', '24.0', '50'])
        writer.writerow(['2023-10-05', '23.5', '58'])

if __name__ == '__main__':
    with tempfile.NamedTemporaryFile(mode='w', suffix='.csv', delete=False) as temp_file:
        temp_path = temp_file.name
    create_sample_csv(temp_path)
    
    try:
        avg_temp = calculate_average_temperature(temp_path)
        print(avg_temp)
    finally:
        os.unlink(temp_path)