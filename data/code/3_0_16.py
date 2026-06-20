import csv
import os
import tempfile

def calculate_average_temperature(file_path):
    if not os.path.exists(file_path):
        raise FileNotFoundError(f"The file {file_path} does not exist.")
    
    temperatures = []
    
    with open(file_path, 'r', newline='') as csvfile:
        reader = csv.reader(csvfile)
        header_found = False
        
        for row in reader:
            if not row:
                continue
            
            try:
                value = float(row[0])
                temperatures.append(value)
                header_found = True
            except ValueError:
                continue
    
    if not temperatures:
        raise ValueError("No valid temperature readings found in the file.")
    
    return sum(temperatures) / len(temperatures)

if __name__ == '__main__':
    sample_content = "10.5\n20.0\n15.5\n30.2\n25.0"
    
    with tempfile.NamedTemporaryFile(mode='w', suffix='.csv', delete=False) as temp_file:
        temp_file.write(sample_content)
        temp_file_path = temp_file.name
    
    try:
        result = calculate_average_temperature(temp_file_path)
        print(result)
    finally:
        os.remove(temp_file_path)