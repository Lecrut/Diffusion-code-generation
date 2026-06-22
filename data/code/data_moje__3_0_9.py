import csv
import os
import tempfile

def calculate_average_temperature(file_path):
    if not os.path.exists(file_path):
        raise FileNotFoundError(f"File {file_path} not found.")
    
    total_temp = 0.0
    count = 0
    
    with open(file_path, 'r', newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        
        if 'temperature' not in reader.fieldnames:
            raise ValueError("CSV file must contain a 'temperature' column.")
            
        for row in reader:
            try:
                value = float(row['temperature'])
                total_temp += value
                count += 1
            except (ValueError, TypeError):
                continue
                
    if count == 0:
        return 0.0
        
    return total_temp / count

def create_sample_csv():
    fd, path = tempfile.mkstemp(suffix='.csv')
    try:
        with os.fdopen(fd, 'w', newline='') as f:
            f.write("temperature\n")
            f.write("10.5\n")
            f.write("20.5\n")
            f.write("30.0\n")
        return path
    except Exception:
        if os.path.exists(path):
            os.remove(path)
        raise

if __name__ == '__main__':
    sample_path = create_sample_csv()
    try:
        result = calculate_average_temperature(sample_path)
        print(result)
    finally:
        if os.path.exists(sample_path):
            os.remove(sample_path)