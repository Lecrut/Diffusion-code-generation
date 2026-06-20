import csv
import os
import tempfile

def celsius_to_fahrenheit(celsius_value):
    return celsius_value * 9 / 5 + 32

def process_temperature_csv(input_path, output_path):
    if not os.path.exists(input_path):
        raise FileNotFoundError(f"Input file {input_path} not found.")

    with open(input_path, mode='r', newline='') as infile:
        reader = csv.reader(infile)
        headers = next(reader)
        
        if not headers or 'temperature_celsius' not in headers:
            raise ValueError("CSV must contain a 'temperature_celsius' header.")
        
        temp_index = headers.index('temperature_celsius')
        new_headers = [h if h != 'temperature_celsius' else 'temperature_fahrenheit' for h in headers]
        
        rows = []
        for row in reader:
            if not row:
                continue
            try:
                celsius_val = float(row[temp_index])
                fahrenheit_val = celsius_to_fahrenheit(celsius_val)
                row[temp_index] = str(round(fahrenheit_val, 2))
            except (ValueError, IndexError):
                continue
            rows.append(row)

    with open(output_path, mode='w', newline='') as outfile:
        writer = csv.writer(outfile)
        writer.writerow(new_headers)
        for row in rows:
            writer.writerow(row)

    return output_path

if __name__ == '__main__':
    input_csv_content = "id,temperature_celsius\n1,0\n2,100\n3,37\n4,20"
    
    fd, temp_input_path = tempfile.mkstemp(suffix='.csv')
    with os.fdopen(fd, 'w') as f:
        f.write(input_csv_content)
    
    fd, temp_output_path = tempfile.mkstemp(suffix='.csv')
    os.close(fd)
    
    result_path = process_temperature_csv(temp_input_path, temp_output_path)
    
    with open(result_path, mode='r') as f:
        content = f.read()
    
    print(content)
    
    os.unlink(temp_input_path)
    os.unlink(temp_output_path)