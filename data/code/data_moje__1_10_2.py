import csv
import io
import os
import tempfile

def safe_float_convert(value):
    if value is None:
        return None
    cleaned = str(value).strip()
    if not cleaned:
        return None
    try:
        return float(cleaned)
    except ValueError:
        return None

def process_weight_data(file_path):
    weights = []
    with open(file_path, 'r', newline='', encoding='utf-8') as f:
        reader = csv.reader(f)
        for row in reader:
            for cell in row:
                converted = safe_float_convert(cell)
                if converted is not None:
                    weights.append(converted)
    if not weights:
        return 0.0
    total = sum(weights)
    count = len(weights)
    return total / count

if __name__ == '__main__':
    sample_csv_content = """weight
10.5
20.3
invalid_data
15.0
7.2
bad_entry
9.8"""
    
    temp_dir = tempfile.gettempdir()
    temp_file_path = os.path.join(temp_dir, 'temp_weights.csv')
    
    with open(temp_file_path, 'w', newline='', encoding='utf-8') as temp_file:
        temp_file.write(sample_csv_content)
    
    result = process_weight_data(temp_file_path)
    print(result)
    os.remove(temp_file_path)