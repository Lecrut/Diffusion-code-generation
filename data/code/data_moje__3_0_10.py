import csv
import os
import tempfile

def calculate_average_temperature(file_path):
    try:
        if not os.path.exists(file_path):
            raise FileNotFoundError(f"The file {file_path} does not exist.")
        
        temperatures = []
        with open(file_path, 'r', newline='', encoding='utf-8') as csvfile:
            reader = csv.reader(csvfile)
            next(reader, None)
            
            for row in reader:
                if not row or not row[0].strip():
                    continue
                try:
                    temp_value = float(row[0].strip())
                    temperatures.append(temp_value)
                except ValueError:
                    continue
        
        if not temperatures:
            raise ValueError("No valid temperature data found in the file.")
        
        return sum(temperatures) / len(temperatures)
    
    except (FileNotFoundError, PermissionError, IOError) as e:
        raise e

if __name__ == '__main__':
    sample_csv_content = """temperature
20.5
22.3
19.8
21.0
23.1
"""
    with tempfile.NamedTemporaryFile(mode='w', delete=False, suffix='.csv', encoding='utf-8') as temp_file:
        temp_file.write(sample_csv_content)
        temp_file_path = temp_file.name
    
    try:
        average_temp = calculate_average_temperature(temp_file_path)
        print(average_temp)
    finally:
        os.remove(temp_file_path)