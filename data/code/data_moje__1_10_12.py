import csv
import io
import os

def calculate_average_weight(file_path):
    if not os.path.exists(file_path):
        raise FileNotFoundError(f"The file {file_path} does not exist")
    
    weights = []
    with open(file_path, 'r', newline='') as csvfile:
        reader = csv.reader(csvfile)
        for row in reader:
            if not row:
                continue
            try:
                value = float(row[0].strip())
                weights.append(value)
            except ValueError:
                continue
    
    if not weights:
        raise ValueError("No valid numeric weight values found in the file")
    
    return sum(weights) / len(weights)

if __name__ == '__main__':
    sample_data = """10.5
20.0
15.7
invalid
30.2
abc
12.4"""
    
    csv_file_path = 'sample_weights.csv'
    with open(csv_file_path, 'w') as f:
        f.write(sample_data)
    
    result = calculate_average_weight(csv_file_path)
    print(f"{result}")
    os.remove(csv_file_path)