import csv
import os

def calculate_average_temperature(filepath):
    if not os.path.exists(filepath):
        raise FileNotFoundError(f"The file {filepath} does not exist.")
    
    total_temp = 0.0
    count = 0
    
    try:
        with open(filepath, 'r', newline='', encoding='utf-8') as file:
            reader = csv.reader(file)
            header = next(reader, None)
            
            for row in reader:
                if not row:
                    continue
                
                temp_str = row[0].strip()
                try:
                    temp = float(temp_str)
                    total_temp += temp
                    count += 1
                except ValueError:
                    continue
        
        if count == 0:
            raise ValueError("No valid temperature readings found in the file.")
        
        return total_temp / count
    
    except IOError as e:
        raise IOError(f"Error reading the file: {e}")

if __name__ == '__main__':
    sample_data_filename = 'temp_readings.csv'
    sample_data_content = [
        "Temperature",
        "23.5",
        "24.0",
        "22.8",
        "Invalid",
        "25.1"
    ]
    
    with open(sample_data_filename, 'w', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        for line in sample_data_content:
            writer.writerow([line])
    
    try:
        average = calculate_average_temperature(sample_data_filename)
        print(f"Calculated Average Temperature: {average:.2f}")
    except Exception as e:
        print(f"An error occurred: {e}")
    
    if os.path.exists(sample_data_filename):
        os.remove(sample_data_filename)