import csv
import os

def scale_volumes(input_filepath, output_filepath, scale_factor):
    rows = []
    with open(input_filepath, 'r', newline='') as infile:
        reader = csv.DictReader(infile)
        for row in reader:
            name = row['name']
            volume = float(row['volume'])
            scaled_volume = volume * scale_factor
            rows.append({'name': name, 'volume': scaled_volume})
    
    with open(output_filepath, 'w', newline='') as outfile:
        fieldnames = ['name', 'volume']
        writer = csv.DictWriter(outfile, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(rows)
    
    return rows

if __name__ == '__main__':
    input_file = 'input.csv'
    output_file = 'output.csv'
    factor = 2.0
    
    sample_data = [
        {'name': 'apple', 'volume': 10.0},
        {'name': 'banana', 'volume': 5.0},
        {'name': 'cherry', 'volume': 20.0}
    ]
    
    with open(input_file, 'w', newline='') as f:
        fieldnames = ['name', 'volume']
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(sample_data)
    
    result = scale_volumes(input_file, output_file, factor)
    
    print(result)
    
    os.remove(input_file)
    os.remove(output_file)